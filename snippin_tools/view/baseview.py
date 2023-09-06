import dataclasses
from typing import Type

import flet as ft
from flet_core import View


@dataclasses.dataclass
class Sized:
    width: int
    height: int


class BaseView:
    pages: dict = {}
    sized: Sized = None

    def __init__(self, root: ft.Page, route):
        self.root = root
        self.route = route
        self.root.on_route_change = self.route_change
        self.root.on_view_pop = self.pop_view
        self.root.on_resize = self.on_resize
        self.root.on_window_event = self.on_window_event
        self.sized = Sized(root.width, root.height)
        if route not in self.pages.keys():
            BaseView.pages[route] = self.get_view()

    def route_change(self, route_event: ft.RouteChangeEvent):
        self.root.views.clear()
        if route_event.route in self.pages.keys():
            self.root.views.append(self.pages[route_event.route])
        self.root.update()

    def get_view(self) -> View:
        return ft.View()

    def setState(self,event=None):
        event() if event != None else event
        self.root.views.remove(self.pages[self.route])
        self.pages[self.route] = self.get_view()
        self.root.views.append(self.pages[self.route])
        self.root.update()

    def pop_view(self, view):
        self.root.views.pop()
        top_view = self.root.views[-1]
        self.root.go(top_view.route)

    def on_resize(self, e: ft.ControlEvent):
        self.sized = Sized(self.root.width, self.root.height)
        self.setState()

    def on_window_event(self, e:ft.ControlEvent):
        pass
