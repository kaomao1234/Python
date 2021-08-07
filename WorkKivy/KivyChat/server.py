from socket import *
from threading import Thread


class MainServer(Thread):
    def __init__(self):
        super().__init__()
        self.host, self.port = gethostbyname(gethostname()), 5000
        self.socketObj = socket(AF_INET, SOCK_STREAM)
        self.socketObj.bind((self.host, self.port))
        self.socketObj.listen()

    def run(self):
        print('waiting for connection')
        Thread(target=self.connectClient).start()

    def connectClient(self):
        while True:
            con, address = self.socketObj.accept()
            if self.recClient(con, address) == False:
                print(f'{address} is exit.')

    def recClient(self, con: socket, address: str):
        try:
            print('connect from', address)
            while True:
                con.send(bytes(input('send text to user :'), 'utf-8'))
        except:
            con.close()
            return False


if __name__ == '__main__':
    MainServer().start()
