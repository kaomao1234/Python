from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.app import App
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_string("""
<ProgBar>:
  
    orientation: 'vertical'
    # Creating the background of the App
    canvas:
        Color:
            rgb: .45, .28, .5
        Rectangle:
            pos: self.pos
            size: self.size
  
    # Providing label to the pg bar
    Label:
        text: '[size=40px]Progress Bar 1 (at .25)[/size]'
        color: .5, 0, .5, 1
        markup: True
  
    # Creating thepg bar of specific value
    ProgressBar:
        value: .25
        min: 0
        max: 1
        pos_hint: {'x':.1}
        size_hint_x: .8
  
    # Providing label to the pg bar
    Label:
        text: '[size=40px]Progress Bar 2 (at .55)[/size]'
        color: .5, 0, .5, 1
        markup: True
  
    # Creating thepg bar of specific value
    ProgressBar:
        value: .55
        min: 0
        max: 1
        pos_hint: {'x':.1}
        size_hint_x: .8
""")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
# The Label widget is for rendering text.

# The ProgressBar widget is used to
# visualize the progress of some task

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the children at the desired location.


# The class whose internal work is in  kv file
class ProgBar(BoxLayout):
    pass

# Create the App Class


class mainApp(App):
    def build(self):
        return ProgBar()


# Create the run
if __name__ == '__main__':
    mainApp().run()
