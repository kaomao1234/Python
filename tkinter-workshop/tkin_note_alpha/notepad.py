from ttkbootstrap import *
from ttkbootstrap.constants import *
from ui.main_window import MainWindow



class Notepad(Window):
    def __init__(self, title="NoteMate", themename="darkly", iconphoto='', size=None, position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1):
        super().__init__(title, themename, iconphoto, size, position, minsize, maxsize, resizable, hdpi, scaling, transient, overrideredirect, alpha)
        MainWindow(self).pack(fill=BOTH,expand=1)
        
        


if __name__ == "__main__":
    Notepad().mainloop()
