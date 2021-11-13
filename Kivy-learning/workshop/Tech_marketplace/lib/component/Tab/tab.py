from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import *
class Tab(MDFloatLayout,MDTabsBase):
    title = StringProperty('0')
    icon = StringProperty('account-check')