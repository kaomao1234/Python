from tkinter.constants import BOTH, CENTER, DISABLED, E, END, NONE, NORMAL
from ttkbootstrap import Style
from tkinter import *
from threading import *
from tkinter import ttk


class App(Style):
    def __init__(self, theme='darkly', themes_file=None, *args, **kwargs):
        super().__init__(theme=theme, themes_file=themes_file, *args, **kwargs)
        self.root = self.master
        self.mainFrame = ttk.Frame(master=self.root)
        self.allPage = {}
        self.root.title('ChatAlpha')
        for i in (LoginPage, ChatPage):
            self.allPage[i] = i(master=self.mainFrame,
                                container=self, root=self.root)
        self.allPage[LoginPage].pack()
        self.mainFrame.pack(fill="both", expand=True)
        self.root.resizable(0, 0)

    def switchPage(self, desPage: ttk.Frame, showPage: ttk.Frame):
        self.allPage[desPage].destroy()
        self.allPage[showPage].pack()


class LoginPage(ttk.Frame):
    getUsername = ''

    def __init__(self, master, container: App, root: Style().master):
        super().__init__(master=master)
        self.root = root
        self.container = container
        self.switchVar = BooleanVar()
        self.nameApp = ttk.Label(
            master=self, text='TkChat', font=('Bauhaus 93', 28, 'normal'))
        self.nameUser = Entry(master=self, width=30, font=(
            'Bahnschrift Condensed', 13))
        self.passUser = Entry(master=self, width=30, font=(
            'Bahnschrift Condensed', 13))
        self.loginBtn = Button(
            master=self, text='Login', state=DISABLED, width=26, command=self.switchPage, font=('Bahnschrift Condensed', 15, 'normal'), bg='#f7f7f7', fg='#292b2c')
        self.themechkBtn = ttk.Checkbutton(master=self, style='primary.Roundtoggle.Toolbutton',
                                           variable=self.switchVar, text='darkly', command=self.switchTheme)
        print(self.getUsername)

    def switchPage(self):
        LoginPage.getUsername = self.nameUser.get()
        self.container.switchPage(LoginPage, ChatPage)

    def bind(self, sequence=None, func=None):
        super().bind(sequence=sequence, func=func)
        self.nameUser.bind('<KeyRelease>', self.btnFocus)
        self.passUser.bind('<KeyRelease>', self.btnFocus)

    def switchTheme(self):  # todo สลับ theme
        if self.switchVar.get() == True:
            self.loginBtn.configure(fg='#f7f7f7', bg='#292b2c')
            self.container.theme_use(themename='flatly')
            self.themechkBtn.configure(text='flatly')
        else:
            self.loginBtn.configure(bg='#f7f7f7', fg='#292b2c')
            self.container.theme_use(themename='darkly')
            self.themechkBtn.configure(text='darkly')

    def pack(self):  # todo วางตำแหน่งของ widget
        super().pack(fill='y', expand=1)
        self.bind()
        self.root.geometry('385x416')
        self.nameApp.grid(row=0, column=0, pady=50)
        ttk.Label(master=self, text='User/Id',
                  font=('Bahnschrift Condensed', 13)).grid(row=1, column=0, sticky='w')
        self.nameUser.grid(row=2, column=0)
        ttk.Label(master=self, text='Password', font=(
            'Bahnschrift Condensed', 13)).grid(row=3, column=0, sticky='w')
        self.passUser.grid(row=4, column=0)
        self.loginBtn.grid(row=5, column=0, pady=10)
        self.themechkBtn.grid(row=6, column=0, sticky='w')

    def btnFocus(self, e):  # todo กำหนด focus ของปุ๋ม เมื่อ ใส่ข้อมูลในช่อง
        getEnUser = self.nameUser.get()
        getEnPass = self.passUser.get()
        if getEnPass and '' not in (getEnUser, getEnPass):
            self.loginBtn.configure(state=NORMAL)
        else:
            self.loginBtn.configure(state=DISABLED)


class ChatPage(ttk.Frame):
    def __init__(self, master, container: App, root):
        super().__init__(master=master)
        self.root = root
        self.container = container
        self.tabUser = ttk.Treeview(self)
        self.textBox = Text(self,state='disabled')
        self.scrolChat = ttk.Scrollbar(self, command=self.textBox.yview)
        self.talkerName = ttk.Label(self)
        self.textBox.configure(yscrollcommand=self.scrolChat.set)

    def pack(self):
        self.bind()
        self.root.resizable(True, True)
        self.root.geometry('380x590')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text=LoginPage.getUsername).grid(row=0, column=0)
        self.tabUser.grid(row=1, column=0)
        self.textBox.grid(row=0,column=1,rowspan=2)
        self.scrolChat.grid(row=0,column=2,rowspan=2,sticky='ns')
        super().pack(expand=1,fill='both')

    def bind(self):
        super().bind(sequence=None, func=None)


if __name__ == '__main__':
    Apprun = App()
    Apprun.root.mainloop()