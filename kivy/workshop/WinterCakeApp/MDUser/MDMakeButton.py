from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.uix.behaviors import CircularRippleBehavior,RectangularRippleBehavior, BackgroundColorBehavior,FakeRectangularElevationBehavior
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivymd.uix.card import MDCard
Builder.load_string("""
<MDButton@MDBoxLayout>:
    elevation_normal: 12
    
""")
        
class MDButton(MDBoxLayout,RectangularRippleBehavior,Button,ButtonBehavior,FakeRectangularElevationBehavior):
    def __init__(self, **kwargs):
        super(MDButton, self).__init__(**kwargs)
        self.size_hint = (0.2,None)
        self.background_color= 0,0,0,0
        self.radius = [20,20]
        self.md_bg_color = [0, 0, 1, 1]
        self.elevation= 36
        
class BaseApp(MDApp):
    def build(self):
        container = MDBoxLayout(orientation='vertical')
        container.add_widget(MDButton(text='hello world'))
        # container.add_widget(Button(text='hello world'))
        return container

BaseApp().run()