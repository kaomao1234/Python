# gray code
from  ttkbootstrap import  Style
from  tkinter import *
binary_get = input()
chk_value = {False: '0', True: '1', ('1', '1'):False, ('0', '0'):True}
gray_code = []
for i in range(len(binary_get)):
    bin_index = len(binary_get) - i
    try:
        gray_code.append(chk_value[chk_value[(binary_get[bin_index], binary_get[bin_index - 1])]])
    except:
        gray_code.append(chk_value[True])
# gray_code.insert(len(binary_get),binary_get[len(binary_get)-1])
print(''.join(gray_code))
