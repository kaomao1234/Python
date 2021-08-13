import time
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from tkinter.filedialog import *
from threading import Thread
from pyautogui import hotkey
import os


class FileBar:  # ! this class have all option in filebar
    def __init__(self, PageText: Text):
        self.PageText = PageText
        self.fileType = (("txt files", "*.txt"), ("all files", "*.*"))
        self.setPath = StringVar()

    def openFile(self):  # todo this method is open and read file.
        getPath = askopenfilename(
            initialdir="/", title="Open file", filetypes=self.fileType)+'.txt'
        file = open(getPath, mode='r')
        self.PageText.delete('1.0', END)
        self.PageText.insert(END, file.read())
        self.setPath.set(getPath)
        file.close()

    def newFile(self):  # todo this method is new file.
        self.PageText.delete('1.0', END)

    def saveFile(self):  # todo this method is save file.
        getPath = self.setPath.get()
        

    def saveAsFile(self):  # todo this method is save file in Directory.
        pass
