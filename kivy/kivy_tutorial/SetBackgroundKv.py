import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
Builder.load_string("""
<Background>:
    id: main_win
    orientation: "vertical"
    spacing: 10
    space_x: self.size[0]/3
    canvas.before:
        Color:
            rgba:(0.5843137254901961, 0.2, 0.8823529411764706, 1.0)
        Rectangle:
            size: root.width, root.height
            pos: self.pos
    Button:
        text: "Click Me"
        pos_hint :{'center_x':0.2, 'center_y':0.2}
        size_hint: .30, 0
        background_color: (0.06, .36, .4, .675)
        font_size: 40
""")

# create a background class which inherits the boxlayout class


class Background(BoxLayout):

    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)
        pass
# Create App class with name of your app


class SampleApp(App):

    # return the Window having the background template.
    def build(self):
        return Background()


# run app in the main function
if __name__ == '__main__':
    SampleApp().run()
