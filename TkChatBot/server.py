from socket import *
from threading import Thread
from tkinter import ttk


class MainServer(Thread):
    def __init__(self):
        super().__init__()
        self.host, self.port = '192.168.1.11', 5000
        self.sockObj = socket(AF_INET, SOCK_STREAM)
        self.sockObj.bind((self.host, self.port))
        self.sockObj.listen()

    def run(self):
        print('waiting for connection')
        for i in range(0, 2):
            Thread(target=self.waitClient).start()

    def waitClient(self):
        while True:
            connection, client_address = self.sockObj.accept()
            print(type(connection))
            if self.recClient(con=connection, cli_add=client_address) == False:
                print(f'{connection} has close.')

    def recClient(self, con:socket, cli_add):
        try:
            print('connection form', cli_add)
            while True:
                recData = con.recv(1024)
                print("received:", recData.decode('utf-8'))
        except:
            con.close()
            return False


if __name__ == '__main__':
    MainServer().start()