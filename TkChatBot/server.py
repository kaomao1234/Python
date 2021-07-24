from socket import *
from threading import Thread


class MainServer(Thread):
    def __init__(self):
        super().__init__()
        self.host, self.port = '192.168.1.4', 5000
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
                recData = con.recv(1024).decode('utf-8')
                if 'name' in recData.split(':'):
                    self.stackUser.update({recData.split(':')[1]: con})
                print(self.stackUser)
                # print("received:", recData)
        except:
            con.close()
            return False

    def distributeUser(self):
        for i, v in self.stackUser:
            pass


if __name__ == '__main__':
    MainServer().start()
