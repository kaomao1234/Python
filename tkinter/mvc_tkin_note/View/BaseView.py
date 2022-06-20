import ttkbootstrap as ttk
from tkinter import *
from View.TextBar import TextBar
from View.StatusBar import StatusBar
from View.MenuBar import MenuBar

class BaseFrame(ttk.Frame):
    def __init__(self,controller,style):
        super().__init__(master=controller)
        self.controller = controller
        self.menuBar = MenuBar(controller,self)
        self.textBar = TextBar(controller,self)
        self.statusBar = StatusBar(controller,self)
    
    def pack(self):
        super().pack(fill='both',expand=1)
        self.menuBar.pack()
        self.textBar.pack()
        self.statusBar.pack()