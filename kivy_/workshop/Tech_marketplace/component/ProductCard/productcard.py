from kivy.uix.button import ButtonBehavior
from kivy.uix.recycleview.datamodel import RecycleDataModelBehavior
from kivymd.uix.card import MDCard
from kivy.properties import *
class ProductCard(MDCard,ButtonBehavior,RecycleDataModelBehavior):
    text = StringProperty('')
    second_text = StringProperty('')
    img_source = StringProperty('')
    when_click = ObjectProperty()
    def __init__(self,**kwargs):
        super(ProductCard, self).__init__(**kwargs)