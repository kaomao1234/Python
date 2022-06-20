import kivy 
from kivy.app import App 
from kivy.lang import Builder
Labelkv = Builder.load_string("""
#: import Window kivy.core.window.Window
Label: 
    text: str(self.font_size)
    # size_hint:None,None
    font_size: (0.75*self.width)-(0.75*self.height)
    # size:self.texture_size
    markup:True
""")

class MyApp(App):
    def build(self):
        # Labelkv.text = 'Hello Guy'
        return Labelkv
if __name__ == '__main__':
    MyApp().run()
    