import importlib
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kaki.app import App

from utils import bcolor
from utils.transition import MDFadeSlideTransition


class WatchDog(App, MDApp):
    DEBUG = 1
    PY_FILE = set()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_app(self, first=False):
        LabelBase.register(name="Garuda", fn_regular="assets/fonts/garuda-book/Garuda Book/Garuda Book.ttf")
        self.init_file()
        Window.bind(
            on_key_down=self.on_keyboard
        )
        import screens.screen as screen
        root = ScreenManager()
        for name, view in screen.screens.items():
            page = view(name=name)
            root.add_widget(page)
            page.switch_to = lambda goto: setattr(root,'current', goto)
        root.transition = MDFadeSlideTransition()
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return root

    def on_keyboard(self, window, keyboard, keycode, text, modifier):
        color = bcolor.bcolors
        if text == "Ĩ":
            # PauseBreak == "Ĩ"
            state = "State"
            print(
                f"{color.OKGREEN}[{color.ENDC}{color.OKCYAN}{state:<7}{color.ENDC}{color.OKGREEN}]{color.ENDC} {color.OKCYAN}Reloading...{color.OKCYAN}")
            self.on_modified()
            self.on_modified()
            self.rebuild()

    def on_modified(self):
        self.init_file()
        for module in self.PY_FILE:
            importlib.reload(module)

    def init_file(self):
        self.KV_FILES = set()
        for root, dirs, files in os.walk(os.getcwd()):
            if 'env' not in root and 'test' not in root:
                for file in files:
                    if file.endswith('.kv'):
                        self.KV_FILES.add(os.path.join(root, file))
                    elif file.endswith('.py') and file != "main.py":
                        path = os.path.join(root, file)
                        module_path = f'{path}'.replace(os.getcwd(), "").replace(
                            "\\", ".").replace(".py", "")[1:]
                        # self.PY_FILE.add(__import__(
                        #     f"{module_path}", fromlist=['']))
                        self.PY_FILE.add(__import__(module_path, fromlist=['']))


class RecipeApp(MDApp):
    def build(self):
        for path in self.init_file():
            Builder.load_file(path)
        self.title = "RecipeApp"
        import screens.screen as screen
        root = ScreenManager()
        for (name, view) in screen.screens.items():
            root.add_widget(view(name=name, switch_to=lambda goto: setattr(root.current, goto)))
        root.transition = MDFadeSlideTransition()
        return root

    @staticmethod
    def init_file():
        kv_file = set()
        for root, dirs, files in os.walk(os.getcwd()):
            if 'env' not in root and 'test' not in root:
                for file in files:
                    if file.endswith('.kv'):
                        kv_file.add(os.path.join(root, file))
        return kv_file


if __name__ == "__main__":
    # RecipeApp().run()
    WatchDog().run()
