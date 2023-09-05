from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.stencilview import StencilView
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.lang import Builder

KV = """
Widget
    canvas.before:
        StencilPush
        Color
            rgba: 0.3, 0.2, 0.4, 1
        Rectangle
            size: 100, 100
        Rectangle
            size: 50, 50
        StencilUse
        Rectangle:
            size: 100, 100
        StencilPop
"""

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()