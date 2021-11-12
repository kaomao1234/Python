# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.screen import MDScreen
# Builder.load_string("""
# <BoxApp@MDScreen>:
#     pos_hint:{'center_x':0.5,'center_y':0.5}
#     MDBoxLayout:
#         spacing: "10"
#         orientation:'vertical'
#         MDRaisedButton:
#             text: "MDRAISEDBUTTON"
#             # md_bg_color: 1, 0, 1, 1
#             radius:[20,20]
#         MDRoundFlatButton:
#             text: "MDROUNDFLATBUTTON"

# """)
# class BoxApp(MDScreen):
#     def __init__(self, **kwargs):
#         super(BoxApp, self).__init__(**kwargs)

# class MApp(MDApp):
#     def build(self):
#         return BoxApp()
# MApp().run()
from kivy.lang import Builder
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

