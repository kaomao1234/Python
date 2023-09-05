import ctypes

import cv2
from PIL import Image

from mss import mss
from numpy import array, flip


def full_screen_capture():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    mon_res = mon = {'left': 0, 'top': 0, 'width': screensize[0], 'height': screensize[1]}
    sct = mss()
    screen_shot = sct.grab(mon_res)
    img = Image.frombytes("RGB", (screen_shot.width, screen_shot.height), screen_shot.rgb)
    array_image = array(img)
    array_image = flip(array_image, axis=2)
    buffer = cv2.flip(array_image, 0).tobytes()
    return array_image, buffer
