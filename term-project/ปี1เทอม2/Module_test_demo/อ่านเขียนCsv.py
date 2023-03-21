import csv  
import os 
print(os.getcwd()) 
try:
    directory = 'TestBase'
    locate_dir = os.getcwd() 
    path = os.path.join(locate_dir,directory) 
    os.mkdir(path)
except:
    pass
user = [{'โรค':'เบาหวาน','ชื่อยา':'Et1','เวลาทานยา':'18:00','ปริมาณยา':'100'},{'โรค':'ความดัน','ชื่อยา':'Et2','เวลาทานยา':'19:00','ปริมาณยา':'200'}]
save_path = os.getcwd()+f'/{directory}'
file_name = 'Data_test.csv' 
select_save = os.path.join(save_path,file_name)
header = ['โรค','ชื่อยา','เวลาทานยา','ปริมาณยา']
f = open(select_save,'a',newline='',encoding='utf8') 
d_test=csv.DictWriter(f,['โรค','ชื่อยา','เวลาทานยา','ปริมาณยา'],restval='ไม่มี')
d_test.writerows(user) 
f.close()