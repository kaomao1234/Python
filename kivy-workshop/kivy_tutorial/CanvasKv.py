import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
Builder.load_string("""
<CanvasWidget>
  
    # Creating Canvas
    canvas:
  
        # Color is blue if button is pressed,
        # otherwise color is red
        Color: 
            rgb: (1, 0, 0, 1) if self.state == 'normal' else (0, 0, 1, 1)
      
        # Rounded rectangle canvas
        RoundedRectangle:
            size: self.size
            pos: self.pos
              
            # Play with these if you want smooth corners for your button
            radius: 100, 100, 100, 100
          
  
    # Print the text when touched or button pressed    
    on_release:print("I have been clicked")
    """)


class CanvasWidget(ButtonBehavior, Label):
    def __init__(self):
        super(CanvasWidget, self).__init__()
        self.bool = True


class MyApp(App):
    def build(self):
        return CanvasWidget()


if __name__ == '__main__':
    MyApp().run()
