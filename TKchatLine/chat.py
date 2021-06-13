import socket
import sys
import queue
import threading as th
from tkinter import *
from tkinter import ttk
import pyautogui
from ttkbootstrap import Style


#
# HOST = socket.gethostbyname(socket.gethostname())
# PORT = 5000
#
# # จากข้อ 1 : สร้าง socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
#
#
# def connect():
#     while True:
#         try:
#             data = s.recv(1024)
#             print(f'Main server {(HOST, PORT)} >>> {data.decode("utf-8")}')
#         except:
#             break
#
#
# connect_serv = th.Thread(target=connect)
# connect_serv.start()
# print('server is connected.')
# while True:
#     msg = input()
#     try:
#         s.sendall(str.encode(msg))
#         if msg == 'q':
#             print(f'{s} is out')
#             s.close()
#             break
#     except:
#         print('Server has close.')
#         time.sleep(3)
#         break
class ThreadClient(th.Thread):
    def __init__(self, fd_lst, chat_board):
        th.Thread.__init__(self)
        self.setDaemon(True)
        self.all_friend = []
        self.chat_board = chat_board
        self.host, self.port = socket.gethostbyname(socket.gethostname()), 5000
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.connect((self.host, self.port))
        self.fd_lst = fd_lst

    def send_msg(self, type_msg):  # This method send message to other client.
        self.socket_obj.sendall(str.encode(type_msg))

    def run(self):  # This method connect to server.
        while True:
            get_msg = self.socket_obj.recv(1024).decode('utf-8')+'\n'
            self.chat_board.configure(state=NORMAL)
            self.chat_board.insert('end', get_msg)
            self.chat_board.configure(state=DISABLED)
            st_tag = '{}.0'.format(int(self.chat_board.index('end-1c').split('.')[0])-1)
            ed_tag = f'{st_tag}+{len(get_msg)}c'
            self.chat_board.tag_add('red_tag', st_tag, ed_tag)


class ChatGui(Style):
    def __init__(self, theme, theme_file=None):
        super(ChatGui, self).__init__(theme=theme, themes_file=theme_file)
        self.root = self.master
        self.root.geometry('656x486')
        self.root.resizable(0, 0)
        self.container = ttk.Frame(self.root)
        self.name_chat = ttk.Label(
            self.container, text='Name_Chat', style='Inverse.TLabel')
        self.configure('msg.Outline.TButton', font=('Helvetica', 20))
        self.send_btn = ttk.Button(self.container, text='Send', style='msg.Outline.TButton', command=self.send_chat)
        self.scroll_chat = ttk.Scrollbar(self.container)
        self.chat_space = ttk.Frame(self.container)
        self.chat_board = Text(
            self.chat_space, yscrollcommand=self.scroll_chat.set, font=('consolas', 15), wrap='word', state=DISABLED)
        self.scroll_chat.configure(command=self.chat_board.yview)
        self.chat_text = Text(
            self.container, wrap='word', height=5, font=('consolas', 13))
        self.tree_user = ttk.Treeview(self.container, columns=('User'), show='headings', selectmode='browse')
        self.tree_user.column('User', anchor='c')
        self.tree_user.heading('User', text='Friend')
        self.chatclient = ThreadClient(self.tree_user, self.chat_board)
        self.chatclient.start()
        self.put_widget()
        self.fix_option()

    def put_widget(self):  # This method put widget in container.
        self.container.pack(fill=BOTH, expand=1)
        self.container.rowconfigure(1, weight=1)
        self.container.columnconfigure(0, weight=1)
        self.name_chat.grid(row=0, column=0, columnspan=2, sticky='ew')
        self.chat_space.grid(row=1, column=0, sticky='nsew')
        self.scroll_chat.grid(row=1, column=1, sticky='ns')
        self.tree_user.grid(row=0, column=2, rowspan=2, sticky='ns')
        self.chat_text.grid(row=2, column=0, columnspan=2)
        self.send_btn.grid(row=2, column=2, sticky='nsew')

    def fix_option(self):  # This method is mapping between Key and function(Method).
        self.root.bind('<Configure>', self.updatesize)
        self.chat_board.tag_configure('red_tag', foreground='red')
        self.root.protocol("WM_DELETE_WINDOW",
                           lambda: sys.exit())

    def send_chat(self):  # This method insert message to Chat.
        msg = self.chat_text.get('1.0', 'end')
        if msg != '\n':
            self.chat_board.configure(state=NORMAL)
            self.chat_board.insert('end', 'My name >> ' + msg)
            self.chatclient.send_msg(msg)
            self.chat_text.delete('1.0', 'end')
            self.chat_board.configure(state=DISABLED)
            self.chat_text.mark_set('insert', '1.0')
        self.chat_text.focus()

    def updatesize(self, e):  # This method fix geometry chat text.
        self.chat_board.place_configure(
            width=self.chat_space.winfo_width(), height=self.chat_space.winfo_height())


if __name__ == '__main__':
    ChatGui('flatly').root.mainloop()
