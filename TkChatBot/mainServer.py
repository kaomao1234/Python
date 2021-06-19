import socket
import threading as th 
import json

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
allclient = {}
s_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_obj.bind((HOST, PORT))
s_obj.listen()
'#---------------------------------------------------------------------------------'


def respon(connection, client_address):
    while True:
        try:
            data = connection.recv(1024)
            byte_to_str = dict(json.loads(json.dumps(data.decode('utf-8'))))
            allclient.update({byte_to_str['name']:(connection,client_address)})
            print(client_address, '>>>', byte_to_str['text'], '\n')
            if byte_to_str == 'q':
                connection.close()
                print('client is out')
                break
        except:
            print(f'{client_address} connect error.')
            connection.close()
            break


def connect(count: int, start: int):
    global client_address
    while True:
        if start < count:
            connection, client_address = s_obj.accept()
            print(f'server has connect with {client_address}')
            print(f'Client {start + 1}')
            start += 1
            connect_client = th.Thread(target=connect, args=(count, start))
            chat_up = th.Thread(target=respon, args=(connection, client_address))
            connect_client.start()
            chat_up.start()
        # send_text = bytes(input(), 'utf-8')
        # for i in list(allclient.keys()):
        #     i.sendall(send_text)


if __name__ == '__main__':
    connect(int(input('Please enter the number of clients you want to connect to. : ')), 0)
