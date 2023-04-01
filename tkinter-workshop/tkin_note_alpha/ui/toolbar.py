import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from threading import Thread


class ToolBar(ttk.Frame):
    def __init__(self, master, style) -> None:
        super().__init__(master, height=22, style=style)

