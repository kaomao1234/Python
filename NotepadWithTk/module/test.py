from tkinter import StringVar
from tkinter import messagebox
from tkinter.constants import END
from tkinter.filedialog import *
import ttkbootstrap as st
from tkinter.ttk import *
import os


class App(st.Style):
    def __init__(self, theme, themes_file=None, *args, **kwargs):
        super().__init__(theme=theme, themes_file=themes_file, *args, **kwargs)
        self.root = self.master





App('darkly').run.mainloop()
