import ttkbootstrap as ttb
from tkinter.ttk import *


class ChatLine(ttb.Style):
    def __init__(self, theme, themes_file=None, *args, **kwargs):
        super().__init__(theme, themes_file=themes_file, *args, **kwargs)
        self.root = self.master
        self.tabroom = Notebook(self.root)
        self.Chatroom = Frame(self.tabroom)
        self.Topic = Label(self.Chatroom,text='title')
        self.drop_widget()

    def drop_widget(self):
        self.Topic.grid(row=0,column=0,sticky='e')
        self.Chatroom.pack()
        self.tabroom.add(self.Chatroom,text='Tab1')
        self.tabroom.pack(expand=1,fill="both")

ChatLine('flatly').root.mainloop()
