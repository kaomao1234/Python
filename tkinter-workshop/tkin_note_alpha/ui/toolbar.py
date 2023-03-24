import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class ToolBar(ttk.Frame):
    def __init__(self, master, style) -> None:
        super().__init__(master, height=22, style=style)

        self.bind("<Configure>", self.on_size)

    def on_size(self, *args):
        self.master.master.update()
        print(self.winfo_width(), self.winfo_height())
        if (self.winfo_width() <= 120):
            self.configure(height=66)
        else:
            self.configure(height=22)
        
