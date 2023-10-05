from screeninfo import get_monitors
import mss
from typing import Callable
import ctypes
import cv2
from PIL import Image
from mss import mss
from numpy import array, flip, frombuffer, uint8
import pprint
import base64


class MainViewModel:
    def __init__(self, listenter: Callable) -> None:
        self.value = 0
        self.listener = listenter

    def on_click(self, e):
        self.value += 1
        self.listener()

    @staticmethod
    def full_screen_capture():
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        mon_res = {'left': 0, 'top': 0,
                   'width': screensize[0], 'height': screensize[1]}
        sct = mss()
        screen_shot = sct.grab(mon_res)
        img = Image.frombytes(
            "RGB", (screen_shot.width, screen_shot.height), screen_shot.rgb)
        array_image = array(img)
        array_image = flip(array_image, axis=2)
        return base64.b64encode(array_image.tobytes()).decode('utf-8')

