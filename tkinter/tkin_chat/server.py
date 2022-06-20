from socket import *
from threading import Thread
import ast


class MainServer(Thread):
    def __init__(self):
        super().__init__()
        self.host, self.port = gethostbyname(gethostname()), 5000
        self.sockObj = socket(AF_INET, SOCK_STREAM)
        self.sockObj.bind((self.host, self.port))
        self.sockObj.listen()
        self.stackUser = {}

    def run(self):
        print('waiting for connection')
        for i in range(0, 2):
            Thread(target=self.waitClient).start()

    def waitClient(self):
        while True:
            connection, client_address = self.sockObj.accept()
            self.stackUser.update()
            if self.recClient(con=connection, cli_add=client_address) == False:
                print('{} has close.'.format(client_address))

    def recClient(self, con: socket, cli_add):
        try:
            print('connection form', cli_add)
            while True:
                recData = ast.literal_eval(con.recv(1024).decode('utf-8'))
                if recData['name'] not in self.stackUser:
                    self.stackUser.update({recData['name']: con})
                    self.distrubeName()
                elif 'text' in recData:
                    self.groupMsg(recData)
                print("received:", recData)
        except:
            con.close()
            return False

    def groupMsg(self, msg: dict):
        for myName, myCon in self.stackUser.items():
            if myName != msg['name']:
                myCon.sendall(str.encode(str(msg)))

    def distrubeName(self):
        for curName, v in self.stackUser.items():
            for oth_name, con in self.stackUser.items():
                if curName != oth_name:
                    v.sendall(bytes(str({'name': oth_name}), 'utf-8'))


if __name__ == '__main__':
    MainServer().start()
