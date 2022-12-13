import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import importlib
import kivy
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp
from pprint import pprint
Window.size = (360, 640)


def find_kv_component():
    path = set()
    for i in os.listdir('component'):
        kv_file = [i if '.kv' in i else None for i in os.listdir(
            'component/{}'.format(i))][0]
        str_path: str
        if kv_file != None:
            str_path = os.path.join('component', i, kv_file)
            path.add(os.path.join(os.getcwd(), str_path))
    return path


def find_kv_lib():
    path = set()
    for i in os.listdir('lib/Screen_kv'):
        path.add(os.path.join(os.getcwd(), 'lib', 'Screen_kv', i))
    return path


def find_lib_classes():
    path = {}
    for i in os.listdir('lib/Screen_kv'):
        name = i.strip('.kv')
        key = name.title()+"Screen"
        path.update({key: f'lib.Screen_py.{name}'})
    return path


def find_component_classes():
    path = {}
    for i in os.listdir('component'):
        path.update({i: f'component.{i}.{i.lower()}'})
    return path


class MyApp(App, MDApp):
    lib_path = find_kv_lib()
    component_path = find_kv_component()
    lib_classes = find_lib_classes()
    component_classes = find_component_classes()
    DEBUG = 1
    KV_FILES = component_path.union(lib_path)
    CLASSES = component_classes | lib_classes
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.icon = 'images/Logo.png'
        self.title = 'MyApp'

    def build_app(self):
        import lib.Screen_py.root
        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(lib.Screen_py.root)
        return lib.Screen_py.root.RootScreen()

    def _rebuild(self, *args):
        if args[1] == 32:
            return self.rebuild()


MyApp().run()