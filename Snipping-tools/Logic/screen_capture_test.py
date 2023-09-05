from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
import PIL.Image as PImage
from kivy.graphics.texture import Texture
import cv2
import ctypes
from numpy import array, flip
import win32gui
from mss import mss

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


class KivyCapture(Image):
    def __init__(self, fps, **kwargs):
        super(KivyCapture, self).__init__(**kwargs)
        self.mon_res = mon = {'left': 0, 'top': 0, 'width': screensize[0], 'height': screensize[1]}
        self.sct = mss()
        self.fps = fps
        self.frame_idx = 0
        # self.update(10)
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        screen_shot = self.sct.grab(self.mon_res)
        img = PImage.frombytes("RGB", (screen_shot.width, screen_shot.height), screen_shot.rgb)
        array_image = array(img)
        array_image = flip(array_image, axis=2)
        buffer = cv2.flip(array_image, 0).tobytes()
        texture = Texture.create(size=(array_image.shape[1], array_image.shape[0]), colorfmt="rgb")
        texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
        self.texture = texture


class KCaptureApp(App):
    def build(self):
        self.my_camera = KivyCapture(fps=60)
        return self.my_camera

    def on_stop(self):
        # without this, app will not exit even if the window is closed
        pass


if __name__ == '__main__':
    KCaptureApp().run()
