import ttkbootstrap as ttk
from tkinter import *
from functools import partial
from Model.HelpModel import HelpModel


class MenuBar(ttk.Frame):
    def __init__(self, controller, master):
        super().__init__(master=master)
        self.controller = controller
        self.fileButton = ttk.Menubutton(
            self, text='File', bootstyle='primary-outline')
        self.editButton = ttk.Menubutton(
            self, text='Edit', bootstyle='primary-outline')
        self.formatButton = ttk.Menubutton(
            self, text='Format', bootstyle='primary-outline')
        self.viewButton = ttk.Menubutton(
            self, text='View', bootstyle='primary-outline')
        self.helpButton = ttk.Menubutton(
            self, text='Help', bootstyle='primary-outline')
        self.fileMenu = Menu(self.fileButton, tearoff=0)
        self.editMenu = Menu(self.editButton, tearoff=0)
        self.formatMenu = Menu(self.formatButton, tearoff=0)
        self.viewMenu = Menu(self.viewButton, tearoff=0)
        self.helpMenu = Menu(self.helpButton, tearoff=0)

    def config(self):
        self.fileButton.configure(menu=self.fileMenu)
        self.editButton.configure(menu=self.editMenu)
        self.formatButton.configure(menu=self.formatMenu)
        self.viewButton.configure(menu=self.viewMenu)
        self.helpButton.configure(menu=self.helpMenu)
    def setter_attrb(self):
        self.textArea: Text = self.controller.mainFrame.textBar.textArea
        self.statusBar = self.controller.mainFrame.statusBar
    def file_menu_config(self):
        fileModel = self.controller.fileModel
        self.fileMenu.add_command(
            label='New', accelerator='Ctrl+N', command=fileModel.new_file)
        self.fileMenu.add_command(
            label='Open...', accelerator='Ctrl+O', command=fileModel.open)
        self.fileMenu.add_command(
            label='Save', accelerator='Ctrl+S', command=fileModel.save)
        self.fileMenu.add_command(
            label='Save as', accelerator='Ctrl+Shift+S', command=fileModel.save_as)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(
            label='Exit', command=self.controller.destroy)

    def edit_menu_config(self):
        editModel = self.controller.editModel
        self.editMenu.add_command(label='Undo', accelerator='Ctrl+Z',
                                   command=partial(self.textArea.event_generate, '<<Undo>>'))
        self.editMenu.add_separator()
        self.editMenu.add_command(
            label="Cut", accelerator='Ctrl+X', command=partial(self.textArea.event_generate, '<<Cut>>'))
        self.editMenu.add_command(
            label="Copy", accelerator='Ctrl+C', command=partial(self.textArea.event_generate, '<<Copy>>'))
        self.editMenu.add_command(
            label="Paste", accelerator='Ctrl+V',
            command=partial(self.textArea.event_generate, '<<Paste>>'))
        self.editMenu.add_command(
            label="Delete", command=partial(self.textArea.event_generate, '<Delete>'))
        self.editMenu.add_separator()
        self.editMenu.add_command(
            label='Find...', accelerator='Ctrl+F', command=editModel.find_word)
        self.editMenu.add_command(
            label='Replace...', accelerator='Ctrl+H', command=editModel.replace_word)
        self.editMenu.add_command(
            label='Go To...', accelerator='Ctrl+G', command=editModel.goto_line)
        self.editMenu.add_separator()
        self.editMenu.add_command(
            label='Select All',command=lambda: self.textArea.tag_add("sel", "1.0", "end"))
        self.editMenu.add_command(
            label='Time/Date', accelerator='F5', command=editModel.stamp_time)

    def format_menu_config(self):
        formatModel = self.controller.formatModel
        boolVar =BooleanVar()
        self.formatMenu.add_checkbutton(label='Word Wrap',variable=boolVar,command = partial(formatModel.wrap_text,boolVar))
        self.formatMenu.add_command(
            label='Font...',command=formatModel.fontText)

    def view_menu_config(self):
        viewModel = self.controller.viewModel
        boolVar = BooleanVar()
        self.viewMenu.add_checkbutton(label='Status bar',variable=boolVar,command=partial(viewModel.wrap_status,boolVar))

    def help_menu_config(self):
        self.helpMenu.add_separator()
        self.helpMenu.add_command(
            label='About',command=partial(HelpModel,self.controller))

    def pack(self):
        self.setter_attrb()
        self.config()
        self.file_menu_config()
        self.edit_menu_config()
        self.format_menu_config()
        self.view_menu_config()
        self.help_menu_config()
        super().pack(fill='x')
        self.fileButton.pack(side='left')
        self.editButton.pack(side='left')
        self.formatButton.pack(side='left')
        self.viewButton.pack(side='left')
        self.helpButton.pack(side='left')
