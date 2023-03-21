# Program to explain how to use Scatter in kivy

# import kivy module
from os import stat
import kivy
from kivy.base import runTouchApp
from kivy.core.text import markup
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.input.motionevent import MotionEvent
from kivy.uix.behaviors import DragBehavior
# from kivy.input.motionevent import MotionEvent
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
# kivy.require('1.9.0')

# Scatter is used to build interactive
# widgets that can be translated,
# rotated and scaled with two or
# more fingers on a multitouch system.

# Widgets are elements of a
# graphical user interface that
# form part of the User Experience.

# This layout allows you to set relative coordinates for children.
Builder.load_file('p.kv')

# # Creating widget class
class SquareWidget(Widget):
    pass

# Creating Scatter Class
class ScatterWidget(Scatter):
    pass

# Create the layout class
class Scatter_App(RelativeLayout):
    pass

class ScatterApp(App):
    def build(self):
        return Scatter_App()

if __name__=='__main__':
    ScatterApp().run()


# class SquareWidget(Widget):
#     def __init__(self, **kwargs):
#         super(SquareWidget, self).__init__(**kwargs)
#         self.size = (100, 100)
#         with self.canvas:
#             Color(rgb=[0.345, 0.85, 0.456])
#             Rectangle(size=self.size, pos=self.pos)


# class ScatterWidget(Scatter):
#     def __init__(self, **kwargs):
#         super(ScatterWidget, self).__init__(**kwargs)
#         self.add_widget(SquareWidget())

# class Scatter_App(RelativeLayout):
#     def __init__(self, **kwargs):
#         super(Scatter_App, self).__init__(**kwargs)
#         with self.canvas:
#             Color(rgb=[.8, .5, .4])
#             Rectangle(size=(800, 600), pos=self.pos)
#         self.square_widget_id = ScatterWidget()
#         self.add_widget(self.square_widget_id)
#         self.square_widget_id.bind(pos=self.callback_pos)
#         self.Label_pos = Label(size_hint=(.1, .1), pos=(500, 300))
#         self.add_widget(self.Label_pos)

#     def callback_pos(self, cls,pos):
#         self.Label_pos.text = 'Position:' + ','.join(list(map(lambda s: str(round(s, 2)),pos)))


# class ScatterApp(App):
#     def build(self):
#         return Scatter_App()


# if __name__ == '__main__':
#     ScatterApp().run()
