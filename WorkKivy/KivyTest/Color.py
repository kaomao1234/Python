from kivy.app import App
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.floatlayout import FloatLayout
parent = FloatLayout()
clr_picker = ColorPicker()
parent.add_widget(clr_picker)

# To monitor changes, we can bind to color property changes
def on_color(instance, value):
    print("RGBA = ", str(value))  #  or instance.color
    print("HSV = ", str(instance.hsv))
    print("HEX = ", str(instance.hex_color))

clr_picker.bind(color=on_color)
class OnApp(App):
    def build(self):
        return parent
App = OnApp()
App.run()