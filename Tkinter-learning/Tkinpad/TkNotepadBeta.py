from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
import time
import os
import re


class MyNotepad:
    root = Tk()
    df_size = 11
    df_font = 'cosolas'
    df_style = 'normal'

    def __init__(self):
        self.root.geometry('400x400')
        self.root.title('TkNotepad')
        self.OptionBar = ttk.Frame(self.root)
        self.TextBox = ttk.Frame(self.root)
        self.StatBar = ttk.Frame(self.root)
        self.X_scrollbar = ttk.Scrollbar(
            self.root, orient='horizontal')
        self.Y_scrollbar = ttk.Scrollbar(
            self.root, orient='vertical')
        self.TextType = Text(self.TextBox, bg='white', font=(self.df_font, self.df_size, self.df_style),
                             xscrollcommand=self.X_scrollbar.set, yscrollcommand=self.Y_scrollbar.set, wrap='none',
                             undo=True)
        self.WorkStat = ttk.Label(
            self.StatBar, text='Ln 1,Col 1', relief='sunken', border=1)
        self.right_menu = Menu(tearoff=0)
        self.OptionMenuBtn = {}

    def dropwidget(self):
        for c in ['File', 'Edit', 'Format', 'View', 'Help']:
            self.OptionMenuBtn.update(
                {c: (ttk.Menubutton(self.OptionBar, text=c), Menu(tearoff=0))})
            self.OptionMenuBtn[c][0].configure(menu=self.OptionMenuBtn[c][1])
            self.OptionMenuBtn[c][0].pack(side=LEFT)
        self.OptionBar.grid(row=0, column=0, sticky='ew', columnspan=2)
        self.TextBox.grid(row=1, column=0, sticky='nsew')
        self.X_scrollbar.grid(row=2, column=0, sticky='ew', columnspan=2)
        self.Y_scrollbar.grid(row=1, column=1, sticky='ns')
        self.WorkStat.pack(side=RIGHT)
        self.StatBar.grid(row=3, column=0, sticky='ew', columnspan=2)

    def set_command(self):
        self.TextType.tag_configure('red_tag', foreground='red', underline=1)
        self.TextType.focus()
        Grid.rowconfigure(self.root, 1, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        self.TextType.bindtags(('Text', 'post-class-bindings', '.', 'all'))
        self.TextType.bind_class(
            'post-class-bindings', '<Key>', self.stat_active)
        self.TextType.bind_class(
            'post-class-bindings', '<Button-1>', self.stat_active)
        self.TextType.bind_class(
            'post-class-bindings', '<Control-MouseWheel>', self.re_fontsize)
        self.TextType.bind_class(
            'post-class-bindings', '<Button-3>', self.right_event)
        self.TextType.bind_class(
            'post-class-bindings', '<B1-Motion>', self.stat_active)
        self.root.bind("<Configure>", self.textsize_config)
        self.X_scrollbar['command'] = self.TextType.xview
        self.Y_scrollbar['command'] = self.TextType.yview
        self.right_menu.add_command(
            label="Cut", accelerator='Ctrl+X', command=lambda: self.TextType.event_generate('<<Cut>>'))
        self.right_menu.add_command(
            label="Copy", accelerator='Ctrl+C', command=lambda: self.TextType.event_generate('<<Copy>>'))
        self.right_menu.add_command(
            label="Paste", accelerator='Ctrl+V', command=lambda: self.TextType.event_generate('<<Paste>>'))
        self.right_menu.add_command(
            label="Delete", command=lambda: self.TextType.event_generate("<Delete>"))
        self.call_option()

    def stat_active(self, e):
        pos_cursor = self.TextType.index(INSERT).split('.')
        self.WorkStat['text'] = 'Ln {},Col {}'.format(
            pos_cursor[0], int(pos_cursor[1]) + 1)

    def textsize_config(self, e):
        # w = int(self.parent.winfo_width() / 3.5)
        # s = 'My Notepad'.rjust(w // 2)
        # self.parent.title(s)
        self.TextType.place_configure(
            width=self.TextBox.winfo_width(), height=self.TextBox.winfo_height())

    def re_fontsize(self, e):
        if e.delta > 0:
            self.df_size += 1
            if self.df_size > 72:
                self.df_size = 72
        else:
            self.df_size -= 1
            if self.df_size < 8:
                self.df_size = 8
        self.TextType['font'] = (self.df_font, self.df_size, self.df_style)

    def right_event(self, event):
        try:
            self.right_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_menu.grab_release()

    def file_menu_btn(self):
        file_obj = FileOption(self.TextType)
        self.OptionMenuBtn['File'][1].add_command(
            label='New', accelerator='Ctrl+N')
        self.OptionMenuBtn['File'][1].add_command(
            label='New Window', accelerator='Ctrl+Shift+N')
        self.OptionMenuBtn['File'][1].add_command(
            label='Open...', accelerator='Ctrl+O', command=lambda: file_obj.save_read(filedialog.askopenfilename(
                initialdir="/", title="Open file", filetypes=(("txt   files", "*.txt"), ("all files", "*.*"))), 'r'))
        self.OptionMenuBtn['File'][1].add_command(
            label='Save', accelerator='Ctrl+S', command=lambda: file_obj.save_read(file_obj.path.get(), 'w'))
        self.OptionMenuBtn['File'][1].add_command(
            label='Save as', accelerator='Ctrl+Shift+S', command=lambda: file_obj.save_read(
                filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                             filetypes=(("txt files", "*.txt"), ("all files", "*.*"))), 'w+'))
        self.OptionMenuBtn['File'][1].add_separator()
        self.OptionMenuBtn['File'][1].add_command(
            label='Exit', command=lambda: self.root.destroy())

    def edit_menu_btn(self):
        index = list(map(lambda s: re.sub(r'\D', '', s),
                         self.WorkStat['text'].split(',')))
        index = '{}.{}'.format(index[0], int(index[1]) - 1)
        stamp_time = time.strftime('%H:%M %p %d/%m/%Y').replace('PM', '')
        edit_obj = EditOption(self.TextType)
        self.OptionMenuBtn['Edit'][1].add_command(label='Undo', accelerator='Ctrl+Z',
                                                  command=lambda: self.TextType.event_generate('<<Undo>>'))
        self.OptionMenuBtn['Edit'][1].add_separator()
        self.OptionMenuBtn['Edit'][1].add_command(
            label="Cut", accelerator='Ctrl+X', command=lambda: self.TextType.event_generate('<<Cut>>'))
        self.OptionMenuBtn['Edit'][1].add_command(
            label="Copy", accelerator='Ctrl+C', command=lambda: self.TextType.event_generate('<<Copy>>'))
        self.OptionMenuBtn['Edit'][1].add_command(
            label="Paste", accelerator='Ctrl+V', command=lambda: self.TextType.event_generate('<<Paste>>'))
        self.OptionMenuBtn['Edit'][1].add_command(
            label="Delete", command=lambda: self.TextType.event_generate("<Delete>"))
        self.OptionMenuBtn['Edit'][1].add_separator()
        self.OptionMenuBtn['Edit'][1].add_command(
            label='Find...', accelerator='Ctrl+F', command=lambda: edit_obj.find_popup())
        self.OptionMenuBtn['Edit'][1].add_command(
            label='Replace...', accelerator='Ctrl+H', command=lambda: edit_obj.replace_popup())
        self.OptionMenuBtn['Edit'][1].add_command(
            label='Go To...', accelerator='Ctrl+G', command=lambda: edit_obj.go_toline())
        self.OptionMenuBtn['Edit'][1].add_separator()
        self.OptionMenuBtn['Edit'][1].add_command(
            label='Select All', accelerator='Ctrl+A', command=lambda: self.TextType.tag_add("sel", "1.0", "end"))
        self.OptionMenuBtn['Edit'][1].add_command(
            label='Time/Date', accelerator='F5', command=lambda: self.TextType.insert(index, stamp_time))

    def format_menu_btn(self):
        wrap_sw = BooleanVar()
        self.OptionMenuBtn['Format'][1].add_checkbutton(label='Word Wrap', command=lambda: self.TextType.configure(
            wrap='word') if wrap_sw.get() else self.TextType.configure(wrap='none'), variable=wrap_sw)
        self.OptionMenuBtn['Format'][1].add_command(
            label='Font...', command=lambda: FormatOption(self.root, self.TextType))

    def view_menu_btn(self):
        status_sw = BooleanVar()
        self.OptionMenuBtn['View'][1].add_checkbutton(label='Status bar',
                                                      command=lambda: self.StatBar.grid_forget() if status_sw.get() else self.StatBar.grid(
                                                          row=3, column=0, sticky='ew', columnspan=2),
                                                      variable=status_sw)

    def help_menu_btn(self):
        self.OptionMenuBtn['Help'][1].add_separator()
        self.OptionMenuBtn['Help'][1].add_command(
            label='About', command=lambda: HelpOption(self.root))

    def call_option(self):
        self.file_menu_btn()
        self.edit_menu_btn()
        self.format_menu_btn()
        self.view_menu_btn()
        self.help_menu_btn()

    @property
    def run(self):
        self.dropwidget()
        self.set_command()
        return self.root


class FileOption:
    parent = MyNotepad.root

    def __init__(self, note_text):
        self.path = StringVar()
        self.NoteText = note_text

    def save_read(self, path, mode):
        file = open(path, mode=mode)
        if mode == 'r':
            self.parent.title('{}'.format(path.split('/')[-1]))
            self.NoteText.delete('1.0', END)
            self.NoteText.insert(END, file.read())
            self.path.set(path)
        elif mode == 'w+':
            file.write(self.NoteText.get('1.0', END))
        else:
            file.write('\n'.join(self.NoteText.get('1.0', END).splitlines()))
        file.close()


class EditOption:
    parent = MyNotepad.root

    def __init__(self, note_text):
        self.NoteText = note_text
        self.all_word = []
        self.idxword = 0
        self.fword = StringVar()
        self.rword = StringVar()
        self.pointline = IntVar()

    def find_popup(self):
        root_find = Toplevel(self.parent)
        root_find.protocol("WM_DELETE_WINDOW",
                           lambda: self.remove_tag(root_find))
        root_find.resizable(width=False, height=False)
        root_find.title('Find...')
        root_find.geometry('365x155')
        root_find.transient(self.parent)
        ttk.Label(root_find, text='Find what: ').grid(
            row=0, column=0, sticky='ns', pady=25, padx=10)
        ttk.Entry(root_find, textvariable=self.fword, width=20).grid(
            row=0, column=1, sticky='nsew', pady=25)
        ttk.Button(root_find, text='Search', command=lambda: self.search_click()).grid(
            row=0, column=2, pady=25, padx=20)
        ttk.Button(root_find, text='Cancel',
                   command=lambda: self.remove_tag(root_find)).grid(row=1, column=2)

    def search_click(self):
        self.all_word.clear()
        self.NoteText.tag_remove('red_tag', '1.0', 'end')
        self.tag_word(self.NoteText.search(
            self.fword.get(), '1.0', END), self.fword)

    def replace_popup(self):
        root_replace = Toplevel(
            master=self.parent)
        root_replace.protocol("WM_DELETE_WINDOW",
                              lambda: self.remove_tag(root_replace))
        root_replace.resizable(width=False, height=False)
        root_replace.geometry('400x200')
        root_replace.title('Replace...')
        root_replace.transient(master=self.parent)
        self.fword.set('')
        ttk.Label(root_replace, text='Find what: ').grid(
            column=0, row=0, sticky='ns', padx=10, pady=25)
        enter_find = ttk.Entry(root_replace, textvariable=self.fword, width=20)
        enter_find.grid(
            row=0, column=1, sticky='nsew', pady=25)
        ttk.Label(root_replace, text='Replace with: ').grid(
            column=0, row=1, padx=10, sticky='ns')
        enter_repl = ttk.Entry(root_replace, textvariable=self.rword, width=20)
        enter_repl.grid(
            row=1, column=1)
        ttk.Button(root_replace, text='Find next', command=lambda: self.search_click()).grid(
            row=0, column=2, pady=25, padx=20)
        ttk.Button(root_replace, text='Replace',
                   command=lambda: self.replace_click(self.fword.get(), self.rword.get())).grid(
            row=1, column=2, )
        ttk.Button(root_replace, text='Replace all', command=lambda: self.replace_allclick(self.rword.get())).grid(
            row=2, column=1, pady=10)
        ttk.Button(root_replace, text='Cancel', command=lambda: self.remove_tag(
            root_replace)).grid(row=2, column=0, pady=10)

    def go_toline(self):
        root_line = Toplevel(self.parent)
        root_line.geometry('300x130')
        root_line.resizable(0, 0)
        root_line.transient(self.parent)
        ttk.Label(root_line, text='Line number:', justify=LEFT).pack(
            side=TOP, anchor=NW, padx=10, pady=10)
        getline = ttk.Entry(root_line, textvariable=self.pointline, width=38,
                            font='consolas 10')
        getline.pack(padx=10, anchor=W)
        ttk.Button(root_line, text='Cancel',
                   command=lambda: root_line.destroy()).pack(side=RIGHT, padx=10)
        ttk.Button(root_line, text='Go to', command=lambda: self.set_cursorpos(
            root_line)).pack(side=RIGHT)
        getline.focus()

    def set_cursorpos(self, root):
        if self.pointline.get() <= int(self.NoteText.index('end-1c').split('.')[0]):
            self.NoteText.mark_set('insert', f'{self.pointline.get()}.0')
            root.destroy()
        else:
            messagebox.showinfo(
                'Notepad - Goto Line', 'The line number is beyond the total number of lines')

    def tag_word(self, start, word):
        offset = '+%dc' % len(word.get())
        end = start + offset
        if start == '' or word.get() == '':
            return
        if (start, end) not in self.all_word:
            self.all_word.append((start, end))
        self.NoteText.tag_add('red_tag', start, end)
        self.tag_word(self.NoteText.search(word.get(), end, END), word)

    def remove_tag(self, root):
        root.destroy()
        self.NoteText.tag_remove("red_tag", "1.0", "end")

    def replace_click(self, fword, rword):
        try:
            before_tag = self.all_word[self.idxword]
            self.NoteText.tag_remove('red_tag', before_tag[0], before_tag[1])
            self.NoteText.delete(before_tag[0], before_tag[1])
            self.NoteText.insert(before_tag[0], rword)
            self.NoteText.tag_add(
                'red_tag', before_tag[0], f'{before_tag[0]}+{len(rword)}c')
            self.idxword += 1
        except:
            messagebox.showinfo(self.parent.wm_title(),
                                'Cannot find {}'.format(f"'{fword}'"))

    def replace_allclick(self, word):
        for i in self.all_word:
            self.NoteText.delete(i[0], i[1])
            self.NoteText.insert(i[0], word)
            self.NoteText.tag_add('red_tag', i[0], f'{i[0]}+{len(word)}c')


class FormatOption(Toplevel):

    def __init__(self, parent, textbox):
        super().__init__(parent)
        self.parent = parent
        self.container = ttk.Frame(self)
        self.textbox = textbox
        self.title('Font')
        self.resizable(0, 0)
        self.transient(self.parent)
        self.fontframe = Frame(self.container)
        ttk.Style(self.fontframe).configure('Treeview', rowheight=30)
        self.styleframe = Frame(self.container)
        self.sizeframe = Frame(self.container)
        self.pretextframe = ttk.LabelFrame(
            self.container, text='Sample', width=370, height=138)
        self.treefont = ttk.Treeview(self.fontframe, show='tree')
        self.treestyle = ttk.Treeview(self.styleframe, show='tree')
        self.listsize = Listbox(self.sizeframe)
        self.fontvar = StringVar()
        self.stylevar = StringVar()
        self.sizevar = StringVar()
        self.searchfont = ttk.Entry(
            self.fontframe, textvariable=self.fontvar, font=('consolas', 10))
        self.searchstyle = ttk.Entry(
            self.styleframe, textvariable=self.stylevar)
        self.searchsize = ttk.Entry(self.sizeframe, textvariable=self.sizevar)
        self.pretext = ttk.Label(self.pretextframe, text='AaBbYyZz',
                                 anchor=CENTER)
        self.fontfamilies = sorted((list(font.families())))
        self.all_style = ['normal', 'italic', 'Bold',
                          'Bold Italic', 'roman', 'underline', 'overstrike']
        self.all_size = [8, 9, 10, 11, 12, 14, 16,
                         18, 20, 22, 24, 26, 28, 36, 48, 72]
        self.fontids = {}
        self.styleids = {}
        self.keep_clicksize = []
        self.keep_typesize = []
        self.active_font = {'font': 'consolas', 'size': 15, 'style': 'normal'}
        self.setwidget()

    def setfont(self):
        for i in self.fontfamilies:
            self.fontids.update(
                {i.lower(): self.treefont.insert('', 'end', text=i, tag=i)})
            self.treefont.tag_configure(i, font=(i, 13))
        self.searchfont.focus()
        self.searchfont.bind(
            '<KeyRelease>', lambda *arg: self.select_font('font'))
        self.treefont.bind('<ButtonRelease-1>',
                           lambda s: self.cur_active('font', tree=self.treefont, search=self.searchfont))
        ttk.Label(self.fontframe, text='Font:').grid(
            row=0, column=0, sticky='w')
        self.searchfont.grid(row=1, column=0, sticky='we', columnspan=2)
        y_bar = Scrollbar(self.fontframe, command=self.treefont.yview)
        self.treefont.configure(yscrollcommand=y_bar.set)
        y_bar.grid(row=2, column=1, sticky='ns')
        self.treefont.grid(row=2, column=0)
        self.fontframe.grid(row=0, column=0)

    def setstyle(self):
        for i in self.all_style:
            self.styleids.update(
                {i.lower(): self.treestyle.insert('', 'end', text=i, tag=i)})
            self.treestyle.tag_configure(i, font=(i, 13))
        self.treestyle.bind(
            '<ButtonRelease-1>', lambda s: self.cur_active('style', self.treestyle, self.searchstyle))
        self.searchstyle.bind(
            '<KeyRelease>', lambda s: self.select_font('style'))
        ttk.Label(self.styleframe, text='Font style:').grid(
            row=0, column=0, sticky='w')
        self.searchstyle.grid(row=1, column=0, sticky='ew', columnspan=2)
        self.treestyle.grid(row=2, column=0)
        self.styleframe.grid(padx=10, row=0, column=1)

    def setsize(self):
        y_bar = Scrollbar(self.sizeframe, command=self.listsize.yview)
        self.listsize.configure(yscrollcommand=y_bar.set)
        for i in self.all_size:
            self.listsize.insert(self.all_size.index(i), i)
        self.searchsize.bind('<KeyRelease>', self.select_size)
        self.listsize.bind('<<ListboxSelect>>', self.click_size)
        y_bar.bind('<B1-Motion>', lambda s: print(self.listsize.yview()[0]))
        ttk.Label(self.sizeframe, text='Size:').grid(
            row=0, column=0, sticky='w')
        self.searchsize.grid(row=1, column=0, columnspan=2, sticky='we')
        self.listsize.grid(row=2, column=0, sticky='ew')
        y_bar.grid(row=2, column=1, sticky='ns')
        self.sizeframe.grid(row=0, column=2, sticky='n')

    def setpretext(self):
        self.pretext.place(x=0, y=0, width=366, height=120)
        self.pretextframe.grid(row=1, column=1, columnspan=2, sticky='news')

    def select_font(self, check):
        selectlst = {}
        word, listfont, tree, ids = None, None, None, None
        if check == 'font':
            word, tree, ids, listfont = self.fontvar.get().lower(
            ), self.treefont, self.fontids, self.fontfamilies
        elif check == 'style':
            word, tree, ids, listfont = self.stylevar.get().lower(
            ), self.treestyle, self.styleids, self.all_style
        for i in listfont:
            if word != '' and word == i[:len(word)].lower():
                selectlst.update({i: ids[i.lower()]})
        try:
            tree.yview_moveto(listfont.index(
                list(selectlst.keys())[0]) * 0.0059)
            tree.selection_set(list(selectlst.values()))
        except:
            tree.selection_remove(tree.selection())

    def cur_active(self, check, tree, search):
        search.delete(0, END)
        getfont = tree.item(tree.focus())['text']
        if check == 'font':
            for i in self.all_style:
                self.treestyle.tag_configure(i, font=(getfont, 15, i.lower()))
            self.active_font.update({'font': getfont})
        else:
            self.active_font.update({'style': getfont})
        self.pretext.configure(
            font=(self.active_font['font'], self.active_font['size'], self.active_font['style'].lower()))
        search.insert('end', getfont)
        search.select_range(0, 'end')
        search.icursor('end')

    def click_size(self, event):
        # var_a = 0
        try:
            var_a = self.listsize.get(self.listsize.curselection()[0])
            self.keep_clicksize.append(var_a)
        except:
            var_a = self.keep_clicksize[len(self.keep_clicksize) - 1]
            self.keep_clicksize.clear()
        self.active_font.update({'size': var_a})
        self.pretext.configure(
            font=(self.active_font['font'], self.active_font['size'], self.active_font['style'].lower()))
        self.searchsize.delete('0', 'end')
        self.searchsize.insert('end', var_a)

    def select_size(self, event):
        font = self.active_font['font']
        size = self.sizevar.get()
        style = self.active_font['style'].lower()
        selectlst = []
        if size != '' and int(size) >= 8:
            self.active_font.update({'size': size})
            self.pretext.configure(font=(font, int(size), style))  # 0.0625
        for i in self.all_size:
            if size == f'{i}'[:len(size)]:
                selectlst.append(i)
        self.listsize.yview_moveto(self.all_size.index(selectlst[0]) * 0.0625)

    def setwidget(self):
        self.setfont()
        self.setstyle()
        self.setsize()
        self.setpretext()
        ttk.Button(self.container, text='Cancel', command=lambda: self.destroy(
        ), width=10).grid(row=2, column=2, sticky='e')
        ttk.Button(self.container, text='OK', width=10, command=lambda: self.config_textbox()).grid(row=2,
                                                                                                    column=1, sticky='e')
        self.container.pack()

    def config_textbox(self):
        font = self.active_font['font']
        size = self.active_font['size']
        style = self.active_font['style'].lower()
        MyNotepad.df_font = font
        MyNotepad.df_size = size
        MyNotepad.df_style = style
        self.textbox.configure(font=(font, size, style))
        self.destroy()


class HelpOption(Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.container = parent
        self.geometry('475x320')
        self.resizable(0, 0)
        self.title('TkNotepad')
        self.transient(self.container)
        pc_name_f = ttk.LabelFrame(
            self, text='Pc name')
        ttk.Label(pc_name_f, text=os.getenv('COMPUTERNAME'), font=(
            'consolas', 20, 'normal')).pack()
        pc_name_f.pack(fill=X)
        library_f = ttk.LabelFrame(
            self, text='Libary:')
        ttk.Label(library_f, text='tkinter\nttkbootstrap\nos\nre\ntime', font=(
            'consolas', 20, 'normal')).pack()
        library_f.pack(fill=X)
        credit_f = ttk.LabelFrame(
            self, text='Developer')
        ttk.Label(credit_f, text='Kaomao นอนเถอะ', font=(
            'consolas', 20, 'normal')).pack(fill=Y)
        credit_f.pack(fill=BOTH)
        ttk.Button(self, text='OK',
                   command=lambda: self.destroy()).pack(fill=X)


if __name__ == '__main__':
    MyProject = MyNotepad().run
    MyProject.mainloop()