import socket
import threading
import ast
import time


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.name: str = None

    def initial_client(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.send(str({'name': self.name}))

    def send(self, msg):
        self.sock.sendall(msg.encode())

    def close(self):
        self.sock.close()

    def recv(self):
        return self.sock.recv(1024).decode()
