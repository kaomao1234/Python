from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import *
from kivymd.uix.behaviors import *
class RectangularButton(RectangularRippleBehavior,ButtonBehavior,BackgroundColorBehavior):
    md_bg_color=1,1,1,1