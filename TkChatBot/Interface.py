from tkinter import *
from tkinter import ttk, Event
from ttkbootstrap import Style
from pyautogui import *
from client import ClientUser


class App(Style):
    def __init__(self, theme='cyborg', themes_file=None, *args, **kwargs):
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
            'Bahnschrift Condensed', 13), text='User1')
        self.passUser = Entry(master=self, width=30, font=(
            'Bahnschrift Condensed', 13), text='12345678')
        self.loginBtn = Button(
            master=self, text='Login', state=DISABLED, width=26, command=self.switchPage,
            font=('Bahnschrift Condensed', 15, 'normal'), bg='#f7f7f7', fg='#292b2c')
        self.themechkBtn = ttk.Checkbutton(master=self, style='primary.Roundtoggle.Toolbutton',
                                           variable=self.switchVar, text='cyborg', command=self.switchTheme)

    def switchPage(self):
        LoginPage.getUsername = self.nameUser.get()
        self.container.switchPage(LoginPage, ChatPage)

    def bind(self, sequence=None, func=None):
        super().bind(sequence=sequence, func=func)
        self.nameUser.bind('<KeyRelease>', self.btnFocus)
        self.passUser.bind('<KeyRelease>', self.btnFocus)

    def switchTheme(self):  # todo สลับ theme
        if self.switchVar.get():
            self.loginBtn.configure(fg='#f7f7f7', bg='#292b2c')
            self.container.theme_use(themename='yeti')
            self.themechkBtn.configure(text='yeti')
        else:
            self.loginBtn.configure(bg='#f7f7f7', fg='#292b2c')
            self.container.theme_use(themename='cyborg')
            self.themechkBtn.configure(text='cyborg')

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

    def btnFocus(self, e: Event):  # todo กำหนด focus ของปุ๋ม เมื่อ ใส่ข้อมูลในช่อง
        getEnUser = self.nameUser.get()
        getEnPass = self.passUser.get()
        if getEnPass and '' not in (getEnUser, getEnPass):
            self.loginBtn.configure(state=NORMAL)
        else:
            self.loginBtn.configure(state=DISABLED)


class ChatPage(ttk.Frame):
    # todo ความสูงที่เพิ่มได้สูงสุดของ textChat 9 ต่ำสุด 4
    def __init__(self, master, container: App, root: Tk):
        super().__init__(master=master)
        self.root = root
        self.container = container
        self.tabUser = ttk.Treeview(
            self, show='headings', columns=('1'))
        self.textShow = Text(self, state='disabled', wrap='word', bg='white')
        self.textType = Text(self, wrap='word', height=4,
                             font='consolas 13', background='white')
        self.scrolChat_board = ttk.Scrollbar(self, command=self.textType.yview)
        self.scrolMsg_board = ttk.Scrollbar(self, command=self.textType.yview)
        self.talkerName = ttk.Label(
            self, text='Group Test', font='consolas 20')
        self.backend = ClientUser
        self.jsonUser = {'name': None, 'text': None}
        self.textShow.configure(yscrollcommand=self.scrolChat_board.set)
        self.textType.configure(yscrollcommand=self.scrolMsg_board.set)

    def extenFunc(self):
        self.tabUser.heading('1', text='All user')
        self.tabUser.column("1", anchor="center")
        self.tabUser.tag_configure('red', foreground='red')
        name = LoginPage.getUsername
        self.jsonUser.update({'name': name})
        self.tabUser.insert('', 'end', values=name + '(me)', tags='red')
        self.backend.sendMsg(str(self.jsonUser))

    def pack(self):
        self.bind()
        self.backend = self.backend(self.textShow, self.tabUser)
        self.extenFunc()
        self.backend.start()
        self.root.resizable(True, True)
        self.root.geometry('380x590')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text=self.jsonUser['name']).grid(row=0, column=0)
        self.tabUser.grid(row=1, column=0, sticky='ns', rowspan=2)
        self.talkerName.grid(row=0, column=1)
        self.textShow.grid(row=1, column=1, sticky='nesw')
        self.textType.grid(row=2, column=1, columnspan=2, sticky='ew')
        self.scrolChat_board.grid(row=1, column=2, sticky='ns')
        self.scrolMsg_board.grid(row=2, column=2, sticky='ns')
        super().pack(expand=1, fill='both')

    def backspace_Event(self, e: Event):
        height = self.textType['height']
        if height > 4:
            height -= 1
            self.textType.configure(height=height)

    def shift_enterEvent(self, e: Event):
        height = self.textType['height']
        checkline = self.textType.index(INSERT).split('.')[0]
        if 9 > int(checkline) >= 4:
            height += 1
            self.textType.configure(height=height)

    def return_Event(self, e: Event):
        msgVar = '{} ==> {}'.format(
            self.jsonUser['name'], self.textType.get('1.0', 'end'))
        self.jsonUser.update({'text': self.textType.get('1.0', 'end')})
        self.backend.sendMsg(str(self.jsonUser))
        self.textShow.configure(state='normal')
        self.textShow.insert('end', msgVar)
        self.textShow.configure(state='disabled')
        self.textType.delete('1.0', 'end')
        self.textType.mark_set('insert', '1.0')
        self.textType.configure(height=4)
        hotkey('backspace')

    def bind(self, **kwargs):
        super().bind(sequence=None, func=None)
        self.root.protocol("WM_DELETE_WINDOW", self.del_window)
        self.textType.bind('<BackSpace>', self.backspace_Event)
        self.textType.bind('<Shift-Return>', self.shift_enterEvent)
        self.textType.bind('<Return>', self.return_Event)

    def del_window(self):
        self.backend.sendMsg('0')
        self.root.destroy()


if __name__ == '__main__':
    Apprun = App()
    Apprun.root.mainloop()