import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.toolbar import ToolBar


class MainWindow(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master, style=DANGER)
        self.toolbar = ToolBar(self, style=LIGHT)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="NSEW")
        self.columnconfigure(0, weight=1)
