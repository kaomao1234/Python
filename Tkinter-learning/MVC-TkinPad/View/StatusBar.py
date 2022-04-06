import ttkbootstrap as ttk
from tkinter import *
class StatusBar(ttk.Frame):
    def __init__(self,controller,master):
        super().__init__(master=master)
        self.currentCursor = ttk.Label(self,text='Ln 1,Col 1')
    def pack(self):
        super().pack(fill='x')
        self.currentCursor.pack(side='left')