from kivymd.app import MDApp
import os
from kivy.core.window import Window
from kivy.lang import Builder
from lib.Root.root import Root
from lib.Onboard.onboard import OnboardScreen
from lib.component.Tab.tab import Tab
Window.size = (360, 640)
path = {
        os.path.join(os.getcwd(),'lib','Root','root.kv'),
        os.path.join(os.getcwd(),'lib','Onboard','onboard.kv'),
}
for i in path:
    Builder.load_file(i)
class MyApp(MDApp):
    def __init__(self,**kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.icon = 'images/Logo.png'
        self.title = 'MyApp'
    
    def build(self):
        return Root()

MyApp().run()