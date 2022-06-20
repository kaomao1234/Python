from kivymd.app import MDApp
from kivy.lang import Builder
kv = '''
MDScreen:
    Carousel:
        direction: 'top'
        MDLabel:
            text: 'Hello'
        MDLabel:
            text: 'Hello'
        MDLabel:
            text: 'Hello'
        GridLayout:
            rows:1
            ScrollView:
                MDList:
                    MDLabel:
                        text: 'HelloList'
                    MDLabel:
                        text: 'HelloList'
                    MDLabel:
                        text: 'HelloList'
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


MyApp().run()
