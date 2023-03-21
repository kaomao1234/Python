import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
Builder.load_string("""
<Widgets>:
    Button:
        text: "Press me"
        on_release: root.btn()
  
# Adding Label, Button to popup
<Popups>:
      
    Label:
        text: "You pressed the button"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}
  
    Button:
        text: "Close the popup"
        # set size of the button
        size_hint: 1, 0.4
        # set position of the button  
        pos_hint: {"x":0, "y":0.1}
        on_press: root.dimissPopup()
        
""")


class Widgets(Widget):
    def btn(self):
        # calling of the show popup function
        show_popup()

# Popup class is defined
# The command of the class is in .kv file


class Popups(FloatLayout):
    def __init__(self, getPop, **kwargs):
        super(Popups, self).__init__(**kwargs)
        self.getPop = getPop

    def dimissPopup(self):
        self.getPop.dismiss()

# create App class


class MyApp(App):
    def build(self):
        # return the widget
        return Widgets()

# define popup function in this we create the popup


def show_popup():
    popupWindow = Popup(
                        size_hint=(None, None), size=(200, 200),auto_dismiss=False)
    show = Popups(popupWindow)
    setattr(popupWindow, 'content', show)

    # open popup window
    popupWindow.open()


class MyApp(App):
    def build(self):
        return Widgets()


if __name__ == '__main__':
    MyApp().run()
