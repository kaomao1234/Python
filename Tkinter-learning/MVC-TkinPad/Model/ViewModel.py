from tkinter import *
import ttkbootstrap as ttk
import os
class ViewModel:
    def __init__(self, controller):
        self.controller = controller
    
    def wrap_status(self,var):
        statusBar = self.controller.mainFrame.statusBar
        if var.get():
            statusBar.pack_forget()
        else:
            statusBar.pack()
