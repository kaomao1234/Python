import ttkbootstrap as ttk
from tkinter import *
from functools import partial


class AskSaveChangeView(ttk.Frame):
    def __init__(self, controller, model,master):
        super().__init__(master=master)
        self.controller = controller
        self.master = master
        self.model = model
        ttk.Label(self, text='Do you want to save changes to \n{}?'.format(
            controller.wm_title()), font=('consolas', 13), bootstyle='default', anchor=CENTER).grid(row=0, column=0, columnspan=3)
        ttk.Button(self, text='Save',
                   bootstyle='outline-primary', command=self.save_btn).grid(row=1, column=0)
        ttk.Button(self, text="Don't save",
                   bootstyle='outline-primary', command=self.destroy_master).grid(row=1, column=1)
        ttk.Button(self, text="Cancel",
                   bootstyle='outline-primary', command=master.destroy).grid(row=1, column=2)

    def save_btn(self):
        self.model.save()
        self.master.destroy()

    def destroy_master(self):
        textArea:Text = self.controller.mainFrame.textBar.textArea
        textArea.delete('1.0', 'end')
        self.master.destroy()

    def pack(self):
        super().pack(expand=1, padx=10)
