from kivy.uix.button import ButtonBehavior
from kivymd.uix.card import MDCard
from kivy.properties import *
class ProductCard(MDCard,ButtonBehavior):
    text = StringProperty('')
    second_text = StringProperty('')
    img_source = StringProperty('')