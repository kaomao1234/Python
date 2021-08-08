from socket import *
from threading import *
import kivy
from kivy.uix import label


class Frontend(Thread):
    def __init__(self, chat_board: label.Label):
        super().__init__()
        self.host, self.port = gethostbyname(gethostname()), 5000
        self.socketObj = socket(AF_INET, SOCK_STREAM)
        self.socketObj.connect((self.host, self.port))
        self.chat_board = chat_board

    def run(self):
        print("Now client has connected server.")
        while True:
            recData = self.socketObj.recv(1024).decode('utf-8')
            self.chat_board.text = self.chat_board.text + \
                f'[color=#FF0000]{recData}[/color]' + '\n'

    def send(self, msg: str):
        if msg == '0':
            self.socketObj.close()
        else:
            self.socketObj.send(bytes(msg, 'utf-8'))


if __name__ == '__main__':
    Frontend().start()
