from kivymd.uix.floatlayout import MDFloatLayout
from functools import partial
from kivy.properties import *
class UnderIconButton(MDFloatLayout):
    btn_icon  = StringProperty('')
    under_text =  StringProperty()
    icon_press = ObjectProperty()
    
    