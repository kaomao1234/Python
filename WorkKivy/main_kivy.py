import kivy 
from kivy import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'minimum_width', '600')
Config.set('graphics', 'minimum_height', '500')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'multisamples', '0')
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import markup
from kivy.core import text
from kivy.app import App
from kivy.utils import get_color_from_hex, rgba

width = 600
height = 500


class Main(Screen):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.name = 'main'
        self.tan1 = tuple(map((lambda s: s/255), [255, 165, 79, 255]))
        self.DarkSeaGreen2 = tuple(
            map((lambda s: s/255), [180, 238, 180, 238]))
        self.firebrick1 = tuple(map(lambda s: s/255, [255, 48, 48, 255]))
        with self.canvas.before:
            Color(rgba=self.DarkSeaGreen2)
            self.rect = Rectangle(size=(600, 500))
        self.Top_text = Label(text='[size=20][color=#ff3030ff]Care-ur-heath(kivy)[/color][/size]', pos_hint={
                              'center_x': .5, 'center_y': .9}, markup=True, size=(293, 30), size_hint=(None, None))
        self.user = Label(text='[size=20][color=#ff3030ff]Username[/color][/size]', pos_hint={
                          'center_x': .3, 'center_y': .8}, markup=True, size=(66, 24), size_hint=(None, None))
        self.password = Label(text='[size=20][color=#ff3030ff]Password[/color][/size]', pos_hint={
                              'center_x': .3, 'center_y': .6}, markup=True, size=(66, 24), size_hint=(None, None))
        self.I_user = TextInput(pos_hint={'center_x': .5, 'center_y': .7},
                                size=(270, 30), size_hint=(None, None), multiline=False)
        self.I_password = TextInput(pos_hint={'center_x': .5, 'center_y': .5}, multiline=False, size=(
            270, 30), size_hint=(None, None))
        self.Login = Button(text="Login", font_size=15, background_color=self.tan1, pos_hint={
                            'center_x': .3, 'center_y': .3}, size_hint=(None, None), size=(101, 45))
        self.Sign_up = Button(text="Sign-up", font_size=15, background_color=self.tan1, pos_hint={
                              'center_x': .7, 'center_y': .3}, size_hint=(None, None), size=(101, 45))
        self.Login.bind(on_press=self.check_login)
        for i in [self.Top_text, self.user, self.password, self.I_user, self.I_password, self.Login, self.Sign_up]:
            self.add_widget(i)

    def check_login(self, event):
        if (self.I_user.text == '') or (self.I_password.text == ''):
            popup = Popup(title='Error', content=Label(text='User or Password invalid.'),
                          auto_dismiss=True, size=(200, 100), size_hint=(None, None))
            popup.open()
        return True


class SignUpPage(Screen):
    def __init__(self, **kwargs):
        super(SignUpPage, self).__init__(**kwargs)
        self.name = 'SignUpPage'
        self.tan1 = tuple(map((lambda s: s/255), [255, 165, 79, 255]))
        self.DarkSeaGreen2 = tuple(
            map((lambda s: s/255), [180, 238, 180, 238]))
        self.firebrick1 = tuple(map(lambda s: s/255, [255, 48, 48, 255]))
        with self.canvas.before:
            Color(rgba=self.DarkSeaGreen2)
            self.rect = Rectangle(size=(600, 500))
        self.topdown = {'[size=18][color=#ff3030ff]Name[/color][/size]': (.15, .8),
                        '[size=18][color=#ff3030ff]Last name[/color][/size]': (.55, .8),
                        '[size=18][color=#ff3030ff]Username[/color][/size]': (.15, .6),
                        '[size=18][color=#ff3030ff]Password[/color][/size]': (.15, .4),
                        '[size=18][color=#ff3030ff]Comfirm a password[/color][/size]': (.6, .4)}
        self.title = Label(text='[size=20][color=#ff3030ff]Create a account[/color][/size]', markup=True,
                           size_hint=(None, None), pos_hint={'center_x': .5, 'center_y': .9})
        self.add_widget(self.title)
        for text, pos in self.topdown.items():
            self.add_widget(Label(text=text, markup=True, size_hint=(None, None), pos_hint={
                            'center_x': pos[0], 'center_y': pos[1]}))
        self.Text_set = {'In_name': (.3, .7), 'In_Lname': (.7, .7), 'In_User': (.3, .5),
                         'In_pass': (.3, .3), 'In_conpass': (.7, .3)}
        self.Text_get = {}
        for key, pos in self.Text_set.items():
            self.Text_get[key] = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={
                'center_x': pos[0], 'center_y': pos[1]})
            self.add_widget(self.Text_get[key])
        self.back = Button(text='Back', font_size=15, background_color=self.tan1, size_hint=(None, None),
                           pos_hint={'center_x': .3, 'center_y': .15}, size=(101, 45))
        self.submit = Button(text='Submit', font_size=15, background_color=self.tan1, size_hint=(None, None),
                             pos_hint={'center_x': .7, 'center_y': .15}, size=(101, 45))
        self.add_widget(self.back)
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.on_text)

    def on_text(self, event):
        check = any(
            list(map(lambda s: self.Text_get[s].text == '', self.Text_get)))
        if check == True:
            popup = Popup(title='Error', content=Label(text='Please fill out all information.'),
                          auto_dismiss=True, size=(300, 100), size_hint=(None, None))
            popup.open()
        elif self.Text_get['In_conpass'].text != self.Text_get['In_pass'].text:
            popup = Popup(title='Error', content=Label(text='Please enter the same password.'),
                          auto_dismiss=True, size=(300, 100), size_hint=(None, None))
            popup.open()


class InfoPage(Screen):
    def __init__(self, **kwargs):
        super(InfoPage, self).__init__(**kwargs)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.login = Main()
        self.sign_up_page = SignUpPage()
        self.add_widget(self.login)
        self.add_widget(self.sign_up_page)
        self.login.Sign_up.bind(on_press=self.change_screen)
        self.sign_up_page.back.bind(on_press=self.change_screen)

    def change_screen(self, event):
        if event.text == 'Sign-up':
            self.transition = SlideTransition(direction='left')
            self.current = self.sign_up_page.name
        elif event.text == 'Back':
            self.transition = SlideTransition(direction='right')
            self.current = self.login.name


class MyApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    MyApp().run()
