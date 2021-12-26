import ttkbootstrap as ttk
from tkinter import *
from functools import partial


class TextBar(ttk.Frame):
    def __init__(self, controller, master):
        super().__init__(master=master)
        self.controller = controller
        self.defaultFont = {'font': 'consolas', 'size': 13, 'style': 'normal'}
        self.textFrame = ttk.Frame(self)
        self.textArea = Text(self.textFrame, undo=True, wrap='none',
                             font=tuple(self.defaultFont.values()))
        self.scrollTextVertical = ttk.Scrollbar(
            self, command=self.textArea.yview)
        self.scrollTextHorizontal = ttk.Scrollbar(
            self, orient='horizontal', command=self.textArea.xview)
        self.right_menu = Menu(tearoff=0)
        self.config()

    def config(self):
        self.textArea.configure(yscrollcommand=self.scrollTextVertical.set,
                                xscrollcommand=self.scrollTextHorizontal.set)
        self.textArea.tag_configure('red_tag', foreground='red', underline=1)
        self.textArea.focus()

    def bindMethod(self):
        self.textArea.bindtags(('Text', 'post-class-bindings', '.', 'all'))
        self.textArea.bind_class(
            'post-class-bindings', '<Key>', self.controller.on_cursor_active)
        self.textArea.bind_class(
            'post-class-bindings', '<Button-1>', self.controller.on_cursor_active)
        self.textArea.bind_class(
            'post-class-bindings', '<Control-MouseWheel>', partial(self.controller.wheelFont_size, self))
        self.textArea.bind_class(
            'post-class-bindings', '<Button-3>', self.rightmenu_squence)
        self.textArea.bind_class(
            'post-class-bindings', '<B1-Motion>', self.controller.on_cursor_active)

    def rightmenu_squence(self, event):
        try:
            self.right_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_menu.grab_release()

    def right_menu_config(self):
        self.right_menu.add_command(
            label="Cut", accelerator='Ctrl+X', command=partial(self.textArea.event_generate, '<<Cut>>'))
        self.right_menu.add_command(
            label="Copy", accelerator='Ctrl+C', command=partial(self.textArea.event_generate, '<<Copy>>'))
        self.right_menu.add_command(
            label="Paste", accelerator='Ctrl+V', command=partial(self.textArea.event_generate, '<<Paste>>'))
        self.right_menu.add_command(
            label="Delete", command=partial(self.textArea.event_generate, '<Delete>'))

    def pack(self):
        self.right_menu_config()
        self.bindMethod()
        super().pack(fill='both', expand=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.textFrame.grid(row=0, column=0, sticky='nsew')
        self.scrollTextVertical.grid(row=0, column=1, sticky='ns')
        self.scrollTextHorizontal.grid(
            row=1, column=0, columnspan=2, sticky='ew')
