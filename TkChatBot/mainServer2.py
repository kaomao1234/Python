import socket
import threading as th
import ast


class SingleServer(th.Thread):
    def __init__(self, num_cli: int):
        th.Thread.__init__(self)
        self.num_cli = num_cli
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 5000
        self.sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_obj.bind((self.host, self.port))
        self.sock_obj.listen()
        self.all_connect = {}

    def run(self):
        print('Server is start.')
        for i in range(self.num_cli):
            mul_con = th.Thread(target=self.connect, args=[i])
            mul_con.start()

    def update_name(self):
        for k in list(self.all_connect.values()):
            print(k)
            k.sendall(bytes(str(list(self.all_connect.keys())), 'utf-8'))

    def connect(self, i: int):
        while True:
            connection, client_address = self.sock_obj.accept()
            mul_res = th.Thread(target=self.respon, args=(
                connection, client_address))
            mul_res.start()
            print(f'server has connect with {client_address}')
            print(f'Client {i + 1}')

    def respon(self, connection, client_address):
        while True:
            data = connection.recv(1024)
            byte_to_str = ast.literal_eval(data.decode('utf-8'))
            self.all_connect.update({self.name: connection})
            print(client_address, '>>>', byte_to_str['text'], '\n')


if __name__ == '__main__':
    SingleServer(2).start()
