from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import *

from uix.colors import Colors

Builder.load_file("./colorwidget.kv")


class ItemColor(MDBoxLayout):
    text = StringProperty()


class Root(MDBoxLayout):
    def __init__(self):
        super().__init__()
        self.colors = None

    def on_kv_post(self, base_widget):
        self.colors = Colors()
        for k, v in self.colors.primaries_dict.items():
            tab = Tab(title=f"{k}")
            self.ids.android_tabs.add_widget(tab)

    def on_tab_switch(self, *args):
        tab = args[1]
        self.colors = Colors()
        self.ids.rv.data = []
        cur_color = self.colors.primaries_dict[tab.title]
        if type(cur_color) == list:
            for i in range(len(cur_color)):
                for key, value in cur_color[i].items():
                    primary_text = "" if key not in [
                        500, 200 if i == 1 else 0] else "(primary)"
                    self.ids.rv.data.append({
                        "md_bg_color": value,
                        "text": f"{tab.title}[{key}]{primary_text}" if i == 0 else f"{tab.title} accent[{key}]{primary_text}",
                    })
        else:
            for key, value in cur_color.items():
                primary_text = "" if key not in [500] else "(primary)"
                self.ids.rv.data.append({
                    "md_bg_color": value,
                    "text": f"{tab.title}[{key}]{primary_text}",
                })


class Tab(MDBoxLayout, MDTabsBase):
    def __init__(self, title: str):
        super().__init__(title=title)


class ColorPaletteApp(MDApp):
    def build(self):
        return Root()


ColorPaletteApp().run()
