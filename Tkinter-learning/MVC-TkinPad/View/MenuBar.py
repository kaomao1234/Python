import ttkbootstrap as ttk
from tkinter import *
from functools import partial


class MenuBar(ttk.Frame):
    def __init__(self, controller, master):
        super().__init__(master=master)
        self.controller = controller
        self.file_btn = ttk.Menubutton(
            self, text='File', bootstyle='outline-primary')
        self.edit_btn = ttk.Menubutton(
            self, text='Edit', bootstyle='outline-primary')
        self.format_btn = ttk.Menubutton(
            self, text='Format', bootstyle='outline-primary')
        self.view_btn = ttk.Menubutton(
            self, text='View', bootstyle='outline-primary')
        self.help_btn = ttk.Menubutton(
            self, text='Help', bootstyle='outline-primary')
        self.file_menu = Menu(self.file_btn, tearoff=0)
        self.edit_menu = Menu(self.edit_btn, tearoff=0)
        self.format_menu = Menu(self.format_btn, tearoff=0)
        self.view_menu = Menu(self.view_btn, tearoff=0)
        self.help_menu = Menu(self.help_btn, tearoff=0)

    def config(self):
        self.file_btn.configure(menu=self.file_menu)
        self.edit_btn.configure(menu=self.edit_menu)
        self.format_btn.configure(menu=self.format_menu)
        self.view_btn.configure(menu=self.view_menu)
        self.help_btn.configure(menu=self.help_menu)
    def setter_attrb(self):
        self.textArea: Text = self.controller.mainFrame.textBar.textArea
        self.statusBar = self.controller.mainFrame.statusBar
    def file_menu_config(self):
        file_model = self.controller.file_model
        self.file_menu.add_command(
            label='New', accelerator='Ctrl+N', command=file_model.new_file)
        self.file_menu.add_command(
            label='Open...', accelerator='Ctrl+O', command=file_model.open)
        self.file_menu.add_command(
            label='Save', accelerator='Ctrl+S', command=file_model.save)
        self.file_menu.add_command(
            label='Save as', accelerator='Ctrl+Shift+S', command=file_model.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label='Exit', command=self.controller.destroy)

    def edit_menu_config(self):
        edit_model = self.controller.edit_model
        self.edit_menu.add_command(label='Undo', accelerator='Ctrl+Z',
                                   command=partial(self.textArea.event_generate, '<<Undo>>'))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(
            label="Cut", accelerator='Ctrl+X', command=partial(self.textArea.event_generate, '<<Cut>>'))
        self.edit_menu.add_command(
            label="Copy", accelerator='Ctrl+C', command=partial(self.textArea.event_generate, '<<Copy>>'))
        self.edit_menu.add_command(
            label="Paste", accelerator='Ctrl+V',
            command=partial(self.textArea.event_generate, '<<Paste>>'))
        self.edit_menu.add_command(
            label="Delete", command=partial(self.textArea.event_generate, '<Delete>'))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(
            label='Find...', accelerator='Ctrl+F', command=edit_model.find_word)
        self.edit_menu.add_command(
            label='Replace...', accelerator='Ctrl+H', command=edit_model.replace_word)
        self.edit_menu.add_command(
            label='Go To...', accelerator='Ctrl+G', command=edit_model.goto_line)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(
            label='Select All',command=lambda: self.textArea.tag_add("sel", "1.0", "end"))
        self.edit_menu.add_command(
            label='Time/Date', accelerator='F5', command=edit_model.stamp_time)

    def format_menu_config(self):
        format_model = self.controller.format_model
        check_btn_var =BooleanVar()
        self.format_menu.add_checkbutton(label='Word Wrap',variable=check_btn_var,command = partial(format_model.wrap_text,check_btn_var))

    def view_menu_config(self):
        self.view_menu.add_checkbutton(label='Status bar')

    def help_menu_config(self):
        self.help_menu.add_separator()
        self.help_menu.add_command(
            label='About')

    def pack(self):
        self.setter_attrb()
        self.config()
        self.file_menu_config()
        self.edit_menu_config()
        self.format_menu_config()
        self.view_menu_config()
        self.help_menu_config()
        super().pack(fill='x')
        self.file_btn.pack(side='left')
        self.edit_btn.pack(side='left')
        self.format_btn.pack(side='left')
        self.view_btn.pack(side='left')
        self.help_btn.pack(side='left')
