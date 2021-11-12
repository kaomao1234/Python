from threading import *
from socket import *
from tkinter import *
from tkinter.ttk import Treeview
import ast


class ClientUser(Thread):
    def __init__(self, Textbox: Text, ListUser: Treeview):
        super().__init__()
        self.host, self.port = gethostbyname(gethostname()), 5000
        self.sockObj = socket(AF_INET, SOCK_STREAM)
        self.sockObj.connect((self.host, self.port))
        self.textShow = Textbox
        self.treeeUser = ListUser
        self.textShow.tag_configure('red_tag', foreground='red')

    def run(self):
        print('now client has connected server.')
        while True:
            recData = self.sockObj.recv(1024).decode('utf-8')
            recData = ast.literal_eval(recData)
            print(recData)
            if 'text' not in recData:
                self.treeeUser.insert(
                    '', 'end', values=recData['name'])
            else:
                insMsg = recData['name']+' ==> '+recData['text']
                self.textShow.configure(state=NORMAL)
                self.textShow.insert('end', insMsg)
                self.textShow.configure(state=DISABLED)
                st_tag = '{}.0'.format(
                    int(self.textShow.index('end').split('.')[0]) - 2)
                ed_tag = f'{st_tag}+{len(insMsg)}c'
                st_tag, ed_tag, self.textShow.tag_add(
                    'red_tag', st_tag, ed_tag)
            print('Server send', recData)

    def sendMsg(self, m: str):
        if m == '0':
            self.sockObj.close()
        try: 
            self.sockObj.sendall(str.encode(m))
        except:
            print('Client is out.')


if __name__ == '__main__':
    ClientUser().start()
