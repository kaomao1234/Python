from tkinter import *


class UserInterFace(Frame):
    def __init__(self, controller):
        super().__init__(master=controller)
        self.controller = controller
        Button(self, text="Button 1", command=self.button1,font=('consolas',25)).pack(fill="both")

    def button1(self):
        self.controller.database.onCurrentTime()
        print(self.controller.database.timeStamp)
