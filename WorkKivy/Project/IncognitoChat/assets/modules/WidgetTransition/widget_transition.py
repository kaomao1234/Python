from kivy.uix.screenmanager import ScreenManager,SlideTransition,CardTransition,SwapTransition,FadeTransition,WipeTransition,FallOutTransition,RiseInTransition,NoTransition
from kivy.properties import StringProperty,NumericProperty
class WidgetTransition(ScreenManager):
    tran = StringProperty("NoTransition")
    duration = NumericProperty(0)
    in_direction= StringProperty()
    out_direction = StringProperty()
    
    def __init__(self,**kwargs):
        super(WidgetTransition, self).__init__(**kwargs)
        self.all_trans = {'SlideTransition':SlideTransition(),
                          'CardTransition':CardTransition(),
                          'SwapTransition':SwapTransition(),
                          'FadeTransition':FadeTransition(),
                          'WipeTransition':WipeTransition(),
                          'FallOutTransition':FallOutTransition(),
                          'RiseInTransition':RiseInTransition(),
                          'NoTransition':NoTransition()}
        
    def add_widget(self,widget):
        self.ids.widget_box.add_widget(widget)
    
    def on_in(self):
        self.transition = self.all_trans[self.tran]
        self.transition.duration = self.duration
        self.transition.direction = self.in_direction
        self.current = 'screen_2'
        
    
    def on_out(self):
        self.transition = self.all_trans[self.tran]
        self.transition.duration = self.duration
        self.transition.direction = self.in_direction
        self.current = 'screen_1'
    