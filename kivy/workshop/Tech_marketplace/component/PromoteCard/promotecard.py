from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import *


class PromoteCard(MDRelativeLayout):
    text = StringProperty('')
    second_text = StringProperty('')
    img_source = StringProperty('')
    card_press = ObjectProperty()
    def __init__(self,**kw):
        super().__init__(**kw)