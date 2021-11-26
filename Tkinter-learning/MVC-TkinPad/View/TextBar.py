import ttkbootstrap as ttk
from tkinter import *


class TextBar(ttk.Frame):
    def __init__(self, controller, master):
        super().__init__(master=master)
        self.textArea = Text(self,undo=True,wrap='none')
        self.scrollTextVertical = ttk.Scrollbar(
            self, command=self.textArea.yview)
        self.scrollTextHorizontal = ttk.Scrollbar(
            self, orient='horizontal', command=self.textArea.xview)
        self.config()

    def config(self):
        self.textArea.configure(yscrollcommand=self.scrollTextVertical.set,
                                xscrollcommand=self.scrollTextHorizontal.set)
        self.textArea.tag_configure('red_tag', foreground='red', underline=1)
        self.textArea.focus()

    def pack(self):
        super().pack(fill='both', expand=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.textArea.grid(row=0, column=0, sticky='nsew')
        self.scrollTextVertical.grid(row=0, column=1, sticky='ns')
        self.scrollTextHorizontal.grid(
            row=1, column=0, columnspan=2, sticky='ew')
