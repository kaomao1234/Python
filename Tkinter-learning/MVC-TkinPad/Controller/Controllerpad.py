import ttkbootstrap as ttk
from tkinter import *
from View.BaseView import BaseFrame
from Model.FileModel import FileModel
from Model.EditModel import EditModel
from Model.FormatModel import FormatModel
from Model.ViewModel import ViewModel


class Controllerpad(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinpad')
        style = ttk.Style()
        self.baseFrame = BaseFrame(self, style)
        self.fileModel = FileModel(self)
        self.editModel = EditModel(self)
        self.formatModel = FormatModel(self)
        self.viewModel = ViewModel(self)
        self.geometry("500x500")
        self.bind("<Configure>", self.configSize)

    def run(self):
        self.baseFrame.pack()
        self.mainloop()

    def on_cursor_active(self, e):
        textArea = self.baseFrame.textBar.textArea
        statusLabel = self.baseFrame.statusBar.ln_col
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
        textFrame = self.baseFrame.textBar.textFrame
        textArea = self.baseFrame.textBar.textArea
        textArea.place_configure(
            width=textFrame.winfo_width(), height=textFrame.winfo_height())
