import socket
import threading as th

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
allclient = {}
s_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_obj.bind((HOST, PORT))
s_obj.listen()

# data = bytes('connected','utf-8')
# while True:
#     print('waiting for connection')
#     connection, client_address = s_obj.accept()
#     allclient.update({client_address: connection})
#     print(allclient)
#     if len(allclient.keys())<2:
#         connection.close()
#     else:
#         data = connection.recv(1024)
#         print('get is ', data)
#         if len(allclient.keys()) == 2:
#             if list(allclient.keys()).index(client_address) == 0:
#                 connection = allclient[list(allclient.keys())[1]]
#             else:
#                 connection = allclient[list(allclient.keys())[0]]
#         else:
#             connection.send(data)
#             connection.close()
'---------------------------------------------------------------------------------'


def respon(connection, client_address):
    while True:
        try:
            data = connection.recv(1024)
            byte_to_str = data.decode('utf-8')
            print(client_address, '>>>', byte_to_str, '\n')
            if byte_to_str == 'q':
                connection.close()
                print('client is out')
                break
        except:
            print('\nclient connect error.')
            connection.close()
            break


def connect(count: int):
    while True:
        connection, client_address = s_obj.accept()
        print(f'Client {count}')
        allclient.update({client_address: connection})
        print(f'server has connect with {client_address}')
        if count < 3:
            count += 1
            connect_client = th.Thread(target=connect, args=[count])
            connect_client.start()
            chat_up = th.Thread(target=respon, args=(connection, client_address))
            chat_up.start()
        send_text = bytes(input(), 'utf-8')
        for i in list(allclient.values()):
            i.sendall(send_text)


if __name__ == '__main__':
    connect(1)
