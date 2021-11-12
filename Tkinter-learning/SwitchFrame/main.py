from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.all_screen = {}
        container = Frame(self)
        self.geometry('480x350')
        for i in [Page1, Page2]:
            self.all_screen[i.__name__] = i(container, self)
            # all_screen[Page1.__name__].pack()
        # print(self.switch_page())
        self.all_screen[Page1.__name__].pack()
        container.pack()


    def switch_page(self,previous,current):
        previous.pack_forget()
        print(self.all_screen[current.__name__])
        self.all_screen[current.__name__].pack()


class Page1(Frame):
    def __init__(self, container, root):
        super().__init__(master=container)
        self.root = root
        self.m_var = IntVar()
        Label(self,text='Page1',font=('consolas',20)).pack()
        # m = Entry(self, textvariable=self.m_var,font=('consolas',20))
        # m.pack()
        Button(self, text='go to page2',font=('consolas',20),command=self.go_to_page_2).pack()
    def go_to_page_2(self):
        self.root.switch_page(self,Page2)
        # self.root.all_screen[Page2.__name__].text.configure(text=self.m_var.get())
    
class Page2(Frame):
    def __init__(self, container, root):
        super().__init__(master=container)
        self.root = root
        self.text = Label(self,text='Page2',font=('consolas',20))
        self.text.pack()
        Button(self, text='go to page1',font=('consolas',20),command= lambda :self.root.switch_page(self,Page1)).pack()
        
App().mainloop()
