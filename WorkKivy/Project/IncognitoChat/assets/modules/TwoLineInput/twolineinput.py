from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty,NumericProperty,ObjectProperty,ListProperty
from kivy.clock import Clock
class TwoLineInput(MDRelativeLayout):
    text = StringProperty('')
    font_name = StringProperty('Roboto')
    font_size = NumericProperty(15)
    bind_text = ObjectProperty()
    text_color = ListProperty([0,0,0,1])
    cursor_color = ListProperty([0.9803921568627451, 0.9803921568627451, 0.9803921568627451, 1.0])
    under_line_color = ListProperty([0,0,0,1])
    helper_text = StringProperty('')
    helper_font_name = StringProperty('Roboto')
    helper_bind_text = ObjectProperty()
    helper_color= ListProperty([0,0,0,1])
    
    def __init__(self, **kwargs):
        super(TwoLineInput, self).__init__(**kwargs)