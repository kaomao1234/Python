import kivy
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.app import App
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

# Program to Show how to create a switch
# import kivy module

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software

# Spinner is a widget that provides a
# quick way to select one value from a set.
# like a dropdown list

# module consists the floatlayout
# to work with FloatLayout first
# you have to import it

# Here for providing colour to the background


# create LayoutClass
class SampBoxLayout(FloatLayout):
    # For Spinner defining spinner clicked function
    def spinner_clicked(self, value):
        print("Language selected is " + value)


Builder.load_string("""
<SampBoxLayout>:
  
    # creating the spinner
    Spinner:
        # Assigning id 
        id: spinner_id
  
        # Callback 
        on_text: root.spinner_clicked(spinner_id.text)
  
        # initially text on spinner
        text: "Python"
  
        # total values on spinner
        values: ["Python", "Java", "C++", "C", "C#", "PHP"]
  
        # declaring size of the spinner
        # and the position of it
        size_hint: None, None
        size: 200, 50
        pos_hint:{'center_x':.5, 'top': 1}
""")

# Make an App by deriving from the App class


class SampleApp(App):
    def build(self):

        # Set the background color for the window
        Window.clearcolor = (0.555, 0.261, .888, 0.5)
        return SampBoxLayout()


# create object for thje Appclass
root = SampleApp()
# run the class
root.run()