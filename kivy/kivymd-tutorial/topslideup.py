from kivymd.app import MDApp
from kivy.lang import Builder
kv = '''
MDScreen:
    Carousel:
        direction: 'right'
        MDLabel:
            text: 'Hello'
        MDLabel:
            text: 'Hello'
        MDLabel:
            text: 'Hello'
        Carousel:
            direction: 'bottom'
            MDLabel:
                text: 'HelloList1'
            MDLabel:
                text: 'HelloList2'
            MDLabel:
                text: 'HelloList3'
            MDLabel:
                text: 'HelloList4'
            MDLabel:
                text: 'HelloList5'
            MDLabel:
                text: 'HelloList6'
            MDLabel:
                text: 'HelloList7'
            MDLabel:
                text: 'HelloList8'
            MDLabel:
                text: 'HelloList9'
            MDLabel:
                text: 'HelloList1'
            MDLabel:
                text: 'HelloList2'
            MDLabel:
                text: 'HelloList3'
            MDLabel:
                text: 'HelloList4'
            MDLabel:
                text: 'HelloList5'
            MDLabel:
                text: 'HelloList6'
            MDLabel:
                text: 'HelloList7'
            MDLabel:
                text: 'HelloList8'
            MDLabel:
                text: 'HelloList9'
    '''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


MyApp().run()
