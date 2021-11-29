import ttkbootstrap as ttk
from tkinter import *
from View.MainScreenView import MainFrame
from Model.FileModel import FileModel
from Model.EditModel import EditModel
from Model.FormatModel import FormatModel
from Model.ViewModel import ViewModel


class Controllerpad(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinpad')
        style = ttk.Style()
        self.mainFrame = MainFrame(self, style)
        self.file_model = FileModel(self)
        self.edit_model = EditModel(self)
        self.format_model = FormatModel(self)
        self.view_model = ViewModel(self)
        self.geometry("500x500")
        self.bind("<Configure>", self.configSize)

    def run(self):
        self.mainFrame.pack()
        self.mainloop()

    def on_cursor_active(self, e):
        textArea = self.mainFrame.textBar.textArea
        statusLabel = self.mainFrame.statusBar.ln_col
        pos = textArea.index(INSERT).split('.')
        statusLabel.configure(text=f'Ln {pos[0]} ,Col {int(pos[1])+1}')

    def wheelFont_size(self, instance, e: Event):
        font = instance.defaultFont
        size = int(font['size'])
        if e.delta > 0:
            size += 1
            size = 100 if size > 100 else size
        else:
            size -= 1
            size = 8 if size < 8 else size
        font['size'] = size
        instance.textArea.configure(font=tuple(font.values()))

    def configSize(self, e):
        textFrame = self.mainFrame.textBar.textFrame
        textArea = self.mainFrame.textBar.textArea
        textArea.place_configure(
            width=textFrame.winfo_width(), height=textFrame.winfo_height())
