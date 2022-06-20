import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software

# The Switch widget is active or inactive
# The state transition of a switch is from
# either on to off or off to on.
from kivy.uix.switch import Switch

# The GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# The Label widget is for rendering text.
from kivy.uix.label import Label
from kivy.lang import Builder
# A Gridlayout with a label a switch
# A class which contains all stuff about the switch
Builder.load_string("""
<SimpleSwitch>:
  
    # creating box layout for better view
    BoxLayout:
        size_hint_y: None
        height: '48dp'
  
        # Adding label to switch
        Label:
            text: 'Switch normal'
  
        # creating the switch
        Switch:
  
            # False means OFF and True means ON
            active: False
              
            # Arranging a callback to the switch
            on_active: root.switch_callback(self, self.active)
  
    # Another for another switch
      
    BoxLayout:
        size_hint_y: None
        height: '48dp'
  
        Label:
            text: 'Switch active'
        Switch:
            active: True
            on_active: root.switch_callback(self, self.active)
  
  
    BoxLayout:
        size_hint_y: None
        height: '48dp'
  
        Label:
            text: 'Switch off & disabled'
              
        Switch:
            # disabled True means After making switch False
            # it is disabled now you cannot change its state
            disabled: True
            active: False
  
    BoxLayout:
        size_hint_y: None
        height: '48dp'
  
        Label:
            text: 'Switch on & disabled'
        Switch:
            disabled: True
            active: True
""")


class SimpleSwitch(GridLayout):

    # number of rows
    rows = 4

    # Callback for the switch state transition
    # Defining a Callback function
    # Contains Two parameter switchObject, switchValue
    def switch_callback(self, switchObject, switchValue):

        # Switch value are True and False
        if(switchValue):
            print('Switch is ON:):):)')
        else:
            print('Switch is OFF:(:(:(')


# Defining the App Class
class SwitchApp(App):
    # define build function
    def build(self):
        # retuen the switch class
        return SimpleSwitch()


# Run the kivy app
if __name__ == '__main__':
    SwitchApp().run()
