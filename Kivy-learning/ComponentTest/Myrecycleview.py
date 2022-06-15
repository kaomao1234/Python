from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.boxlayout import BoxLayout
Builder.load_string("""
<MyElement>:
    buttonText:''
    Button:
        id:btn
        text:root.buttonText
        size_hint: (1, None)
        halign:'center'
        valign: "center"
        on_texture_size: root.callTextureSize(self)
        
<Myview>:
    viewclass: 'MyElement'
    orientation:'vertical'
    spacing: 40
    padding:10, 10
    space_x: self.size[0]/3
    RecycleBoxLayout:
        color:(0, 0.7, 0.4, 0.8)
        default_size: None, None
  
        # defines the size of the widget in reference to width and height
        default_size_hint: 1, None 
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical' # defines the orientation of data items
""")


class MyElement(BoxLayout, RecycleDataViewBehavior):
    _latest_data = None
    _rv = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = None
        self.tempHeight = None

    def on_press(self,instance:Button):
        self._latest_data['buttonText'] = ''
        self._rv.refresh_from_data()
    
    def callTextureSize(self, instance:Button):
        self.tempHeight = max(100, instance.texture_size[1]+20)
        instance.height = self.tempHeight
        self.on_height(self, self.height)

    def refresh_view_attrs(self, rv: RecycleView, index, data: dict):
        self._rv = rv
        self.index = index
        self._latest_data = data
        super(MyElement, self).refresh_view_attrs(rv, index, data)

    def on_height(self, instance, value):
        data = self._latest_data
        if(data != None and (self.tempHeight != None and self.tempHeight != self.height)):
            data['height'] = self.tempHeight
            self.height = self.tempHeight


class Myview(RecycleView):
    def __init__(self, **kwargs):
        super(Myview, self).__init__(**kwargs)
        self.data = self.data = [
            {'height': 50, 'buttonText': self.result(x)} for x in range(20)]

    def result(self, x):
        first = 'hello'
        first += f'\n{first}' * x
        return first


class MyApp(App):
    def build(self):
        return Myview()


MyApp().run()
