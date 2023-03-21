import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
Builder.load_string("""
<CustLabel@Label>:
    color: .761, .190, .810, 1
 
<SampBoxLayout>:
    orientation: "vertical"
    padding: 10
    spacing: 10
  
    CustLabel:
        text: "Gender"
        size_hint_x: 1
        font_size:20
 
    # creating box layout
    BoxLayout:
        # assigning orentation
        orientation: "horizontal"
        height: 20
 
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .22
 
            # label creation
            CustLabel:
                text: "Male"
                size_hint_x: .80
                font_size:30
            CheckBox:
                color:.294, .761, .623
                on_active: root.checkbox_click(self, self.active)
                size_hint_x: .20
 
            CustLabel:
                text: "Female"
                size_hint_x: .80
                font_size:20
            CheckBox:
                on_active: root.checkbox_click(self, self.active)
                size_hint_x: .20
 
            CustLabel:
                text: "Other"
                size_hint_x: .80
                font_size:10
            CheckBox:
                on_active: root.checkbox_click(self, self.active)
                size_hint_x: .20
                """)


class SampBoxLayout(BoxLayout):

    # Callback for the checkbox
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")


# App derived from App class
class SampleApp(App):
    # build is a method of Kivy's App class used
    # to place widgets onto the GUI.
    def build(self):
        # setting up window background color
        Window.clearcolor = (0, 0, .30, .60)
        return SampBoxLayout()


# Rum the app
if __name__ == '__main__':
    SampleApp().run()
