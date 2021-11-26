from tkinter import *
class FormatModel:
    def __init__(self, controller):
        self.controller = controller
        self.textArea: Text = self.controller.mainFrame.textBar.textArea
    
    def wrap_text(self,var):
        if var.get():
            self.textArea.configure(wrap='word')
        else:
            self.textArea.configure(wrap='none')
        
    