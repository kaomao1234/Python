from threading import *
from socket import *
from tkinter import *
from tkinter.ttk import Treeview
import sys


class ClientUser(Thread):
    def __init__(self, Textbox: Text, ListUser: Treeview):
        super().__init__()
        self.host, self.port = '192.168.1.4', 5000
        self.sockObj = socket(AF_INET, SOCK_STREAM)
        self.sockObj.connect((self.host, self.port))
        self.boolTask = True

    def run(self):
        print('now client has connected server.')
        self.connected()

    def sendMsg(self, m: str):
        self.sockObj.sendall(str.encode(m))

    def exitClient(self):
        self.boolTask = False
        self.join()

    def connected(self):
        while self.boolTask:
            try:
                recData = self.sockObj.recv(1024).decode('utf-8')
                print('Server send', recData)
            except:
                print('Server has close.')
                self.sockObj.close()
                break


if __name__ == '__main__':
    ClientUser().start()
