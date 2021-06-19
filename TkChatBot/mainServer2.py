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

    def connect(self, i):
        while True:
            connection, client_address = self.sock_obj.accept()
            self.all_connect.update({connection: client_address})
            mul_res = th.Thread(target=self.respon, args=(connection, client_address))
            mul_res.start()
            print(f'server has connect with {client_address}')
            print(f'Client {i + 1}')
            print(th.active_count())

    def respon(self, connection, client_address):
        while True:
            try:
                data = connection.recv(1024)
                byte_to_str = ast.literal_eval(data.decode('utf-8'))
                self.all_connect.update({self.name: connection})
                print(client_address, '>>>', byte_to_str['text'], '\n')
            except:
                print(f'{client_address} is exit.')
                connection.close()
                break


if __name__ == '__main__':
    SingleServer(2).start()
