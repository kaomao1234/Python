from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import *
from functools import partial
class SalesFlatButton(MDRelativeLayout):
    product_name = StringProperty('')
    cheapen_text = StringProperty('')
    btn_click = ObjectProperty()
    img_source = StringProperty('')
    
    