import time
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from tkinter.filedialog import *
from threading import Thread
from pyautogui import hotkey
import os


class MyTkNotepad(Style):  # ! todo This class is main process
    def __init__(self, theme=None, themes_file=None, *args, **kwargs):
        super().__init__(theme=theme, themes_file=themes_file, *args, **kwargs)
        self.root = self.master
        self.root.geometry('400x400')
        self.root.title('TkNotepad')

        self.MenuObj = MenuBar(self.root)
        self.PageObj = PageBar(self.root)
        self.StateObj = StatusBar(self.root)
        self.MenuObj.grid(self.PageObj.PageText,
                          self.update_cursor, self.StateObj)
        self.PageObj.grid()
        self.StateObj.grid()
        self.bind()

    def bind(self):  # todo this method is binding event and key.
        self.PageObj.PageText.bindtags(
            ('Text', 'post-class-bindings', '.', 'all'))
        self.root.bind("<Configure>", self.PageObj.textsize_config)
        self.PageObj.PageText.bind_class(
            'post-class-bindings', '<Key>', self.update_cursor)
        self.PageObj.PageText.bind_class(
            'post-class-bindings', '<Button-1>', self.update_cursor)
        self.PageObj.PageText.bind_class(
            'post-class-bindings', '<Control-MouseWheel>', self.update_fontsize)
        self.PageObj.PageText.bind_class(
            'post-class-bindings', '<B1-Motion>', self.update_cursor)

    # todo this method is update position cursor.

    def update_cursor(self, e=None):
        curHere = self.PageObj.PageText.index(INSERT).split('.')
        curText = self.StateObj.curText.format(curHere[0], int(curHere[1])+1)
        self.StateObj.cursor_bar.configure(text=curText)

    def update_fontsize(self, e):  # todo this method is update font size.
        get_font = self.StateObj.arrFont
        make_font = get_font[0]
        make_size = int(get_font[1])
        make_style = get_font[2]
        if e.delta > 0:
            make_size += 1
            make_size = 100 if make_size > 100 else make_size
        else:
            make_size -= 1
            make_size = 8 if make_size < 8 else make_size
        self.PageObj.PageText.configure(
            font=(make_font, make_size, make_style))
        self.StateObj.font_bar.configure(
            text=self.StateObj.fontText.format(make_font, make_size, make_style))
        self.StateObj.arrFont = (make_font, make_size, make_style)


class MenuBar(ttk.Frame):  # ! this class is MenuBar
    def __init__(self, master):
        super().__init__(master=master)
        # * this variable is mapping name button and menu event.
        self.MapMenu = {}
        self.PageText = None
        self.update_cursor = None
        self.StateObj = None
        self.wrapVar = BooleanVar()
        self.statSwap_Var = BooleanVar()

    def grid(self, PageText: Text, setCur, StateObj):
        super().grid(row=0, column=0, sticky='ew', columnspan=2)
        self.PageText = PageText
        self.update_cursor = setCur
        self.StateObj = StateObj
        for i in ['File', 'Edit', 'Format', 'View', 'Help']:
            Menu_btn = ttk.Menubutton(self, text=i)
            menu = Menu(Menu_btn, tearoff=0)
            self.MapMenu.update({i: menu})
            Menu_btn.configure(menu=menu)
            Menu_btn.pack(side='left')
        for j in [self.addFile_command, self.addEdit_command, self.addFormat_command, self.addHelp_command, self.addView_command]:
            Thread(target=j).start()

    # todo this method is add command in File button.
    def addFile_command(self):
        self.MapMenu['File'].add_command(
            label='New', accelerator='Ctrl+N')
        self.MapMenu['File'].add_command(
            label='Open...', accelerator='Ctrl+O')
        self.MapMenu['File'].add_command(
            label='Save', accelerator='Ctrl+S')
        self.MapMenu['File'].add_command(
            label='Save as', accelerator='Ctrl+Shift+S')
        self.MapMenu['File'].add_separator()
        self.MapMenu['File'].add_command(
            label='Exit')

    # todo this method is add command in Edit button.
    def addEdit_command(self):
        self.MapMenu['Edit'].add_separator()
        self.MapMenu['Edit'].add_command(
            label="Cut", accelerator='Ctrl+X')
        self.MapMenu['Edit'].add_command(
            label="Copy", accelerator='Ctrl+C')
        self.MapMenu['Edit'].add_command(
            label="Paste", accelerator='Ctrl+V')
        self.MapMenu['Edit'].add_command(
            label="Delete")
        self.MapMenu['Edit'].add_separator()
        self.MapMenu['Edit'].add_command(
            label='Find...', accelerator='Ctrl+F')
        self.MapMenu['Edit'].add_command(
            label='Replace...', accelerator='Ctrl+H')
        self.MapMenu['Edit'].add_command(
            label='Go To...', accelerator='Ctrl+G')
        self.MapMenu['Edit'].add_separator()
        self.MapMenu['Edit'].add_command(
            label='Select All', accelerator='Ctrl+A')
        self.MapMenu['Edit'].add_command(
            label='Time/Date', accelerator='F5', command=self.insertTime)

    # todo this method is add command in Format button.
    def addFormat_command(self):
        self.MapMenu['Format'].add_checkbutton(
            label='Word Wrap', variable=self.wrapVar, command=self.setPageText_wrap)
        self.MapMenu['Format'].add_command(
            label='Font...')

    # todo this method is add command in View button.
    def addView_command(self):
        self.MapMenu['View'].add_checkbutton(
            label='Status bar', variable=self.statSwap_Var, command=self.setStat_swap)

    # todo this method is add command in Help button.
    def addHelp_command(self):
        self.MapMenu['Help'].add_separator()
        self.MapMenu['Help'].add_command(
            label='About')

    def insertTime(self):  # todo this method is insert current time.
        getTime = time.strftime('%H:%M %p %d/%m/%Y').replace('PM', '')
        self.PageText.insert(self.PageText.index(INSERT), getTime)
        self.update_cursor()

    def setPageText_wrap(self):  # todo this method is set PageText wrap word.
        if self.wrapVar.get():
            self.PageText.configure(wrap='word')
        else:
            self.PageText.configure(wrap='none')

    def setStat_swap(self):
        if self.statSwap_Var.get():
            self.StateObj.grid_forget()
        else:
            self.StateObj.grid()


class PageBar(ttk.Frame):  # ! this class is PageBar.
    def __init__(self, master):
        super().__init__(master=master)
        self.root = master
        self.PageText = Text(self, wrap='none', undo=True,
                             font='consolas 11 normal')
        self.x_scrollPage = ttk.Scrollbar(
            self.root, orient='horizontal', style='Horizontal.TScrollbar', command=self.PageText.xview)
        self.y_scrollPage = ttk.Scrollbar(
            self.root, orient='vertical', style='Vertical.TScrollbar', command=self.PageText.yview)
        self.PageText.configure(
            xscrollcommand=self.x_scrollPage.set, yscrollcommand=self.y_scrollPage.set)
        # * define right_menu for right click event.
        self.right_menu = Menu(tearoff=0)

    def grid(self):
        self.bind()
        Grid.rowconfigure(self.root, 1, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        super().grid(row=1, column=0, sticky='nsew')
        self.x_scrollPage.grid(row=2, column=0, sticky='ew', columnspan=2)
        self.y_scrollPage.grid(row=1, column=1, sticky='ns')

    def bind(self):
        super().bind()
        self.addRightclick_command()
        self.PageText.tag_configure('red_tag', foreground='red', underline=1)
        self.PageText.bind_class(
            'post-class-bindings', '<ButtonPress-3>', self.right_event)

    # todo this method is update size of self.PageText.
    def textsize_config(self, e):
        self.PageText.place_configure(
            width=self.winfo_width(), height=self.winfo_height())

    # todo this method is add command to right self.right_menu.
    def addRightclick_command(self):
        self.right_menu.add_command(
            label="Cut", accelerator='Ctrl+X', command=lambda: self.PageText.event_generate('<<Cut>>'))
        self.right_menu.add_command(
            label="Copy", accelerator='Ctrl+C', command=lambda: self.PageText.event_generate('<<Copy>>'))
        self.right_menu.add_command(
            label="Paste", accelerator='Ctrl+V', command=lambda: self.PageText.event_generate('<<Paste>>'))
        self.right_menu.add_command(
            label="Delete", command=lambda: self.PageText.event_generate("<Delete>"))

    def right_event(self, event):  # todo this method is right click event.
        try:
            self.right_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_menu.grab_release()


class StatusBar(ttk.Frame):  # ! this class is StatusBar
    def __init__(self, master):
        super().__init__(master=master)
        self.cursor_bar = Label(self, relief='sunken',
                                border=1, font=('consolas', 12))
        self.font_bar = Label(self, relief='sunken',
                              border=1, font=('consolas', 12))
        self.arrFont = ('consolas', '11', 'normal')
        self.curText = 'Ln {},Col {}'
        self.fontText = '{} {} {}'

    def grid(self):
        super().grid(row=3, column=0, sticky='ew', columnspan=2)
        self.cursor_bar.configure(text=self.curText.format(1, 1))
        self.font_bar.configure(
            text=self.fontText.format(self.arrFont[0], self.arrFont[1], self.arrFont[2]))
        self.cursor_bar.pack(side=LEFT)
        self.font_bar.pack(side=LEFT, padx=10)


if __name__ == '__main__':
    MyTkNotepad().root.mainloop()
