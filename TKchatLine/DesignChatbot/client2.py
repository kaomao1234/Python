import socket 
HOST =  socket.gethostbyname(socket.gethostname()) 
PORT = 5000
 
# จากข้อ 1 : สร้าง socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST,PORT)) 
a = 'connect'
while True:
    if a == 'connect':
        a = input('client 2 type : ')
    s.sendall(str.encode(a))
    data = s.recv(1024)
    print(data)