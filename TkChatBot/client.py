from threading import *
from socket import *


class ClientUser(Thread):
    def __init__(self):
        super().__init__()
        self.host, self.port = '192.168.1.11', 5000
        self.sockObj = socket(AF_INET, SOCK_STREAM)
        self.sockObj.connect((self.host, self.port))
        self.connect = Thread(target=self.connected)
        self.connect.start()

    def run(self):
        print('now client has connected server.')
        while True:
            m = input()
            self.sockObj.sendall(str.encode(m))
            if m.lower() == 'e':
                print(self.sockObj, 'is out')
                self.sockObj.close()
                break

    def connected(self):
        while True:
            try:
                recData = self.sockObj.recv(1024)
                print('Server send', recData)
            except:
                print('Server has close.')
                break


if __name__ == '__main__':
    ClientUser().start()
