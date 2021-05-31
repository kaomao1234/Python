import socket 
HOST = socket.gethostbyname(socket.gethostname()) 
PORT = 5000
s_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_obj.bind((HOST,PORT))
s_obj.listen() 
while True : 
    print('waiting for connection')
    connection,client_address = s_obj.accept() 
    try:
        while True:
            data = connection.recv(1024)
            if data:
                connection.sendall(data) 
            else:
                print("no more data from", client_address)  
                break 
    finally:
        connection.close() 
        
                