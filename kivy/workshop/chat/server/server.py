import socket
from threading import Thread
import time
import ast


class Server:
    def __init__(self, host, port, slot: int):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.slot = slot
        self.all_client = {}
        self.sock.listen()

    def wait_lst_client(self):
        serv_name = input("Server name: ")
        print(f'Server is ready...')
        number_of_client = int(input("Number of client: "))
        for i in range(number_of_client):
            client, addr = self.sock.accept()
            Thread(target=self.handle_client, args=(client, addr)).start()

    def boardcast(self, msg):
        for (name, client) in self.all_client.items():
            client.sendall(msg.encode())

    def handle_client(self, client, addr):
        connected = True
        while True:
            print("waiting for message...")
            initial_msg = client.recv(1024).decode()
            initial_msg = ast.literal_eval(initial_msg)
            if(initial_msg['name'] not in list(self.all_client.keys())):
                print(f'{initial_msg["name"]} is already connected')
                self.all_client[initial_msg['name']] = client
                self.boardcast(
                    str({"total_user": list(self.all_client.keys())}))
                break
        try:
            while connected:
                message = client.recv(1024).decode()
                self.boardcast(message)
        except:
            print(f'{addr} is disconnected')
            client.close()


if __name__ == '__main__':
    server = Server('localhost', 9999, 2)
    server.wait_lst_client()
