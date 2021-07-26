import socket
import threading as th
import time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000

# จากข้อ 1 : สร้าง socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def connect():
    while True:
        try:
            data = s.recv(1024)
            print('data is ', data)
            print('true')
        except:
            break

connect_serv = th.Thread(target=connect)
connect_serv.start()
print('server is connected.')
s.sendall(str.encode('name:K1'))
while True:
    msg = input()
    s.sendall(str.encode(msg))
    if msg == 'q':
        print(f'{s} is out')
        s.close()
        break
