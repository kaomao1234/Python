from kivy.app import App

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the children at the desired location.
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_string('''

<SliderWidget>:
  
    # creating the Slider
    Slider:
          
        # giving the orientation of Slider
        orientation: "vertical"
        min: 0  # minimum value of Slider
        max: 100 # maximum value of Slider
        value: 0  # initial value of Slider
  
        # when slider moves then to increase value
        on_value:label1.text = str(int(self.value))
  
    # Adding label
    Label:
        id: label1
        font_size: "30sp"
        text: "0"
        color: 1, 0, 0, 1
  
    Slider:
        orientation: "horizontal"
        min: 0
        max: 100
        value: 30
        on_value:label2.text = str(int(self.value))
          
  
    Label:
        id: label2
        font_size: "30sp"
        text: "30"
        color: 0, 0, 1, 1
''')


# creating the root widget used in .kv file
class SliderWidget(BoxLayout):
    pass

# class in which name .kv file must be named Slider.kv.
# or creating the App class


class Slider(App):
    def build(self):
        # returning the instance of SliderWidget class
        return SliderWidget()


# run the app
if __name__ == '__main__':
    Slider().run()
