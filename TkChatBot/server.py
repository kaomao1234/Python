from socket import *
from threading import Thread
import ast

class MainServer(Thread):
    def __init__(self):
        super().__init__()
        self.host, self.port = gethostbyname(gethostname()), 5000
        print()
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
                print(recData)
                if recData['name'] not in list(self.stackUser.keys()):
                    self.stackUser.update({recData['name']: con})
                elif 'text' in list(recData.keys()):
                    self.distributeUser(recData) 
                print("received:", recData)
        except:
            con.close()
            return False

    def distributeUser(self,msg:dict):
        for i, v in self.stackUser.items():
           if i != msg['name']:
               v.sendall(str.encode(msg['name']+'==>'+msg['text']))


if __name__ == '__main__':
    MainServer().start()
