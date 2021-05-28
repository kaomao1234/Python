from kivy import Config
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex, rgba
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'minimum_width', '600')
Config.set('graphics', 'minimum_height', '500')
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage

class CustomLayout(Screen):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)
        with self.canvas.before:            
            # Color(rgb=get_color_from_hex('#013220'))
            Color(rgb=get_color_from_hex('#90EE90'))
            Rectangle(size=(600,500))
class MainApp(App):

    def build(self):
    
        return CustomLayout()

if __name__ == '__main__':
    MainApp().run()