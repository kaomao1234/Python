from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
<Line1>:
    size_hint_y: None
    canvas:
        Color:
            rgba:get_color_from_hex("#9b4f4f")
        Line:
            width:1
            rectangle:(self.x,self.y,self.width,0)
    Label:
        text:'This is Line.'
        center:root.center
""")
class Line1(Widget):
    pass
class MApp(App):
    def build(self):
        root = BoxLayout()
        m = AnchorLayout(anchor_y="center",anchor_x='center')
        m.add_widget(Line1())
        root.add_widget(m)
        return root
if __name__ == '__main__':
    MApp().run()