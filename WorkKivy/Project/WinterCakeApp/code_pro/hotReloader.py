from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (360, 640)
KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

BoxLayout:
    HotReloadViewer:
        path:app.path_to_kv_file
        errors:True
        errors_text_color:0,0,0,1
        errors_background_color:app.theme_cls.bg_dark
'''


class Example(MDApp):
    path_to_kv_file = 'sign_up.kv'

    def build(self):
        print("Auto reload.")
        return Builder.load_string(KV)


Example().run()
