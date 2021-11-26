import ttkbootstrap as ttk
from tkinter import *
from View.MainScreenView import MainFrame
from Model.FileModel import FileModel
from Model.EditModel import EditModel
from Model.FormatModel import FormatModel
class Controllerpad(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinpad')
        style = ttk.Style()
        self.mainFrame = MainFrame(self,style)
        self.file_model = FileModel(self)
        self.edit_model = EditModel(self)
        self.format_model = FormatModel(self)
    
    def run(self):
        self.mainFrame.pack()
        self.mainloop()