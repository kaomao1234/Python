from tkinter import *
import Views.ui1 as ui
import Models.db as db

class Controller(Tk):

    def __init__(self):
        super().__init__()
        self.title("Controller")
        self.database = db.DataBase()
        frame1 = ui.UserInterFace(self)
        frame1.pack(expand=True, fill="both")

    def start(self):
        self.mainloop()
