from tkinter import *
class App(Tk):
    def __init__(self):
        super().__init__()
        self.container = Frame(self)
        self.screen = {}
        for i in [Page1,Page2]:
            name_frame = i.__name__
            print(name_frame,' == ',i)
            self.screen[name_frame] = i(self.containe,self)
        self.container.pack()
        
    def switch_page(self,previous,current):
        previous.pack_forget()
        self.all_screen[current.__name__].pack()
        
class Page1(Frame):
    def __init__(self,container, root):
        super().__init__(master=container)

class Page2(Frame):
    def __init__(self,container,root):
        super().__init__(master=container)
# root = Tk()

App().mainloop()