import kivy
from kivy import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '1200')
Config.set('graphics', 'minimum_height', '600')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'multisamples', '0')
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.core.text import markup
import re
# Window.size = (1200, 600)


class WidgetProperty(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgetProperty, self).__init__(**kwargs)
        self.size = (200, 600)
        self.size_hint = (None, None)
        self.orientation = 'vertical'
        self.WidgetProperty = Label(
            text='[size=18]Properties', markup=True)
        self.add_widget(self.WidgetProperty)
        self.Pro_text_lst = ['Text', 'Font_size', 'Pos(x,y)', 'Size']
        self.Pro_dict = {}
        for i in self.Pro_text_lst:
            self.add_widget(Label(text=f'[size=14]{i}[/size]', markup=True))
            self.Pro_dict.update({i: TextInput(multiline=False)})
            self.add_widget(self.Pro_dict[i])


class DropWidget(Screen):
    def __init__(self, **kw):
        super(DropWidget, self).__init__(**kw)
        self.size = (800, 600)
        self.size_hint = (None, None)
        with self.canvas:
            Color(rgb=get_color_from_hex('#EEE8AA'))
            Rectangle(size=self.size)   


class ToolBox(GridLayout):
    def __init__(self, **kwargs):
        super(ToolBox, self).__init__(**kwargs)
        self.size = (200, 600)
        self.size_hint = (None, None)
        with self.canvas.before:
            Color(rgb=get_color_from_hex('#90EE90'))
            Rectangle(size=self.size)
        self.size_hint = (None, None)
        self.rows = 2
        self.tool_bar = DropDown()
        self.tool_drop = Button(
            text='Toolbar', font_size=18, size_hint=(1, None))
        self.label_btn = Button(
            text='+Label', font_size=14, height=44, size_hint_y=None)
        self.TInput_btn = Button(
            text='+TextInput', font_size=14, height=44, size_hint_y=None)
        self.Button_btn = Button(
            text='+Button', font_size=14, height=44, size_hint_y=None)
        for i in [self.label_btn, self.TInput_btn, self.Button_btn]:
            i.bind(on_release=lambda btn: self.tool_bar.select(btn.text))
            self.tool_bar.add_widget(i)
        self.tool_bar.bind(on_release=self.tool_bar.open)
        self.tool_bar.bind(on_select=lambda instance, x: setattr(instance, 'text', x))
        self.add_widget(self.tool_drop)


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # self.orientation = 'horizontal'
        self.size = (1200, 600)
        self.allwidget = {}
        # self.size_hint = (None, None)
        self.ToolBoxins = ToolBox()
        self.Screen_ins = DropWidget()
        self.Tab_WidgetProperty = WidgetProperty()
        self.orientation = 'horizontal'
        self.add_widget(self.ToolBoxins)
        self.add_widget(self.Screen_ins)
        self.add_widget(self.Tab_WidgetProperty)
        self.ToolBoxins.label_btn.bind()
        self.Text = self.Tab_WidgetProperty.Pro_dict['Text']
        self.Fontsize = self.Tab_WidgetProperty.Pro_dict['Font_size']
        self.Position = self.Tab_WidgetProperty.Pro_dict['Pos(x,y)']
        self.Size_hw = self.Tab_WidgetProperty.Pro_dict['Size']

    def on_press(self, event):
        on_move = Scatter()
        if event.text == '+Label':
            labelcreated = Label(
                text=f'[size={self.Fontsize.text}]{self.Text.text}', markup=True)
            on_move.add_widget(labelcreated)
            on_move.bind()
            self.allwidget[on_move] = labelcreated
            self.Screen_ins.add_widget(on_move)
            self.Text.text = ''
            self.Fontsize.text = ''

    def callback_pos(self, base, pos_value):
        if pos_value[0] >= 0 and pos_value[1] >= 0:
            if pos_value[0] > self.Screen_ins.size[0]-base.size[0]:
                base.pos = (self.Screen_ins.size[0]-base.size[0], pos_value[1]) 
            elif pos_value[1] > self.Screen_ins.size[1]-base.size[1]:
                base.pos = (pos_value[0],self.Screen_ins.size[1]-base.size[1]) 
            self.Text.text =  re.sub(r'[size=\d]', '', self.allwidget[base].text)
            self.Fontsize.text = ''.join(
                re.findall('\d', self.allwidget[base].text))
            self.Size_hw.text = ','.join(map(str, self.allwidget[base].size))
            self.Position.text = ','.join(
                map(lambda s: str(round(s, 2)), base.pos))
        else:
            if pos_value[0] < 0:
                base.pos = (0, pos_value[1])
            elif pos_value[1] < 0:
                base.pos = (pos_value[0], 0)


class DesignApp(App):
    def build(self):
        return MainScreen()


ins_de = DesignApp()
ins_de.run()
