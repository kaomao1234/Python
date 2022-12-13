from logging import disable
from kivymd.uix.screen import MDScreen
from kivy.properties import *
from kivy.animation import Animation
from kivy.utils import get_color_from_hex as hex
from kivymd.uix.snackbar  import Snackbar
class DetailScreen(MDScreen):
    title = StringProperty('')
    def __init__(self,**kw):
        super(DetailScreen, self).__init__(**kw)
        
    def on_color_choose(self,this,this_color):
        disable_color = [0,0,0,0]
        enable_color = hex('#0001FC')
        parent = this.parent
        anim_disable = Animation(rgba=disable_color,duration=0.1)
        anim_enable = Animation(rgba=enable_color,duration=0.1)
        for i in parent.children:
            if i != this:
                other_color = i.canvas.before.children[0]
                anim_disable.start(other_color)
            else:
                anim_enable.start(this_color)
        
    def on_cap_choose(self,parent,this):
        disable_color = hex('#A7A9BE')
        enable_color = hex('#0001FC')
        anim_disable = Animation(text_color=disable_color,duration=0.1)
        anim_enable = Animation(text_color=enable_color,duration=0.1)
        for i in parent.children:
            if i.text != this.text:
                anim_disable.start(i)
            else:
                anim_enable.start(i)