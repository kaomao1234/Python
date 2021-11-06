from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.clock import Clock
from time import sleep
class IntroScreen(MDScreen):
    def __init__(self,**kw):
        super(IntroScreen, self).__init__(**kw)
        Clock.schedule_once(self.animate_widget,2)
        
    
    def  animate_widget(self,*e):
        for i in  self.ids:
            widget = self.ids[i]
            duration = (list(self.ids.keys()).index(i)+1)*0.2
            center_y = widget.pos_hint['center_y']
            anim = Animation(pos_hint={'center_y':abs(center_y)},duration=duration)
            anim.start(widget)
            # Clock.schedule_once(lambda s : anim.start(widget),0.3)