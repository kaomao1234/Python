import socket
import sys
import threading as th
from tkinter import *
from tkinter import ttk
import ast
import json
from ttkbootstrap import Style


class ThreadClient(th.Thread):  # ! this class is send and get info to server.
    def __init__(self, fd_lst, chat_board, name_user):
        th.Thread.__init__(self)
        self.setDaemon(True)
        self.all_friend = []
        self.chat_board = chat_board
        self.host, self.port = socket.gethostbyname(socket.gethostname()), 5000
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.connect((self.host, self.port))
        self.fd_lst = fd_lst
        self.name_user = name_user

    def send_msg(self, type_msg):  # todo this method is send text
        self.socket_obj.sendall(str.encode(type_msg))

    def run(self):  # todo this method is connect server.
        while True:
            get_msg = self.socket_obj.recv(1024).decode('utf-8')
            print(get_msg)
            # self.chat_board.configure(state=NORMAL)
            # self.chat_board.insert('end', get_msg + '\n')
            # self.chat_board.configure(state=DISABLED)
            # st_tag = '{}.0'.format(
            #     int(self.chat_board.index('end-1c').split('.')[0]) - 1)
            # ed_tag = f'{st_tag}+{len(get_msg)+1}c'
            # self.chat_board.tag_add('red_tag', st_tag, ed_tag)


class ChatUi(ttk.Frame):  # ! this class is Chate page
    name_var = ''

    def __init__(self, style):
        self.root = style.master
        super(ChatUi, self).__init__(master=self.root)
        self.style = style 
        self.style.configure("Treeview", rowheight=int(2.5*15))
        self.name_chat = ttk.Label(
            self, text=self.name_var, style='Inverse.TLabel', font=('consolas', 20))
        self.style.configure('msg.Outline.TButton', font=('Helvetica', 20))
        self.send_msgbtn = ttk.Button(
            self, text='Send', style='msg.Outline.TButton', command=self.send_chat)
        self.scroll_chat = ttk.Scrollbar(self)
        self.chat_frame = ttk.Frame(self)
        self.chat_board = Text(
            self.chat_frame, yscrollcommand=self.scroll_chat.set, font=('consolas', 15), wrap='word', state=DISABLED)
        self.scroll_chat.configure(command=self.chat_board.yview)
        self.msg_text = Text(
            self, wrap='word', height=5, font=('consolas', 13))
        self.tree_user = ttk.Treeview(self, columns=(
            'User'), show='headings', selectmode='browse')
        self.tree_user.column('User', anchor='c')
        self.tree_user.heading('User', text='Friend')
        self.tree_user.insert(
            '', 'end', values=self.name_var+'(me)', tag='user')
        self.tree_user.tag_configure(
            'user', foreground='red', font=('consolas', 15))
        self.chatclient = ThreadClient(
            self.tree_user, self.chat_board, self.name_var)
        self.chatclient.start()
        self.user_api = {"name": f"{self.name_var}"} 
        self.chatclient.send_msg(str(self.user_api))
        self.put_widget()
        self.fix_option()

    def put_widget(self):  # todo this method is put widget in page
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.name_chat.grid(row=0, column=0, columnspan=2, sticky='ew')
        self.chat_frame.grid(row=1, column=0, sticky='nsew')
        self.scroll_chat.grid(row=1, column=1, sticky='ns')
        self.tree_user.grid(row=0, column=2, rowspan=2, sticky='ns')
        self.msg_text.grid(row=2, column=0, columnspan=2)
        self.send_msgbtn.grid(row=2, column=2, sticky='nsew')

    def fix_option(self):  # todo this method is binding between widget and function
        self.root.bind('<Configure>', self.updatesize)
        self.chat_board.tag_configure('red_tag', foreground='red')
        self.root.protocol("WM_DELETE_WINDOW",
                           lambda: sys.exit())

    def send_chat(self):  # todo this method is send text to show chat board
        self.user_api.update({'text': self.msg_text.get('1.0', 'end')})
        msg = self.user_api['text']
        if msg != '\n':
            self.chat_board.configure(state=NORMAL)
            self.chat_board.insert('end', 'My name >> ' + msg)
            self.chatclient.send_msg(str(self.user_api))
            self.msg_text.delete('1.0', 'end')
            self.chat_board.configure(state=DISABLED)
            self.msg_text.mark_set('insert', '1.0')
        self.msg_text.focus()

    def updatesize(self, e):  # todo this method is fix chat geometry
        self.chat_board.place_configure(
            width=self.chat_frame.winfo_width(), height=self.chat_frame.winfo_height())

    def pack(self):
        self.root.geometry('656x486')
        self.root.resizable(0, 0)
        super(ChatUi, self).pack(fill=BOTH,expand=1)


class Login(ttk.Frame):  # ! this class is Login page

    def __init__(self, style):
        self.root = style.master
        super(Login, self).__init__(master=self.root)
        self.style = style
        self.style.configure('msg.Outline.TButton', font=('Helvetica', 20))
        ttk.Label(self, text='Login', font=('consolas', 20),
                  anchor=CENTER).pack(fill=X, expand=1)
        self.put_name = ttk.Entry(self, font=('consolas', 15))
        self.btn_test = ttk.Button(
            self, text='Submit', command=self.switch_frame, style='msg.Outline.TButton')
        self.put_widget()

    def put_widget(self):
        self.put_name.pack(fill=X)
        self.btn_test.pack()

    def pack(self):
        self.root.geometry('300x200')
        super(Login, self).pack(fill=BOTH, expand=1)

    def switch_frame(self):  # todo this method is switch page
        ChatUi.name_var = self.put_name.get()
        self.style.switch_frame(self, ChatUi)


class RunApp(Style):
    def __init__(self):
        super(RunApp, self).__init__()
        self.theme = 'flatly'
        self.root = self.master
        Login(self).pack()

    def switch_frame(self, current_frame, n_frame):
        current_frame.destroy()
        n_frame(self).pack()


if __name__ == '__main__':
    RunApp().root.mainloop()
