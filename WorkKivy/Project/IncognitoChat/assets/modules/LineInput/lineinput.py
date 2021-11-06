from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import ListProperty,NumericProperty,ObjectProperty
class LineInput(MDRelativeLayout):
    under_line_color = ListProperty([0,0,0,1])
    text_color = ListProperty([0,0,0,1])
    font_size = NumericProperty(15)
    bind_text = ObjectProperty()
    cursor_color = ListProperty([0.9803921568627451, 0.9803921568627451, 0.9803921568627451, 1.0])
    def __init__(self,**kwargs):
        super(LineInput,self).__init__(**kwargs)