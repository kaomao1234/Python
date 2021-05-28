import pyautogui 
import numpy as np
size = list(pyautogui.size())
# pyautogui.screenshot('ss.png',region=(0,0,size[0],size[1]))
# print(pyautogui.screenshot(region=(0,0,100,100)))
# ss = pyautogui.screenshot(region=(86,32,2,3))
# ss = np.array(ss)
# print(ss)
# print(ss.shape)
while True:
    print(pyautogui.pixel(*pyautogui.position()))