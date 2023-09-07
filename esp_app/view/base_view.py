import dataclasses
from typing import Type

import flet as ft


@dataclasses.dataclass
class Sized:
    width: int
    height: int


class BaseView:
    """A base class for managing views in a GUI application."""
    pages: dict = {}
    sized: Sized = None

    def __init__(self, root: ft.Page, route):
        """
        Initialize a BaseView instance.

        Args:
            root (ft.Page): The root page of the GUI.
            route: The initial route for this view.
        """
        self.root = root
        self.route = route
        self.root.on_route_change = self.route_change
        self.root.on_view_pop = self.pop_view
        self.root.on_resize = self.on_resize
        self.root.on_window_event = self.on_window_event
        self.sized = Sized(root.width, root.height)
        self.root.views.append(self.get_view())
        if route not in self.pages.keys():
            BaseView.pages[route] = self.get_view()

    def route_change(self, route_event: ft.RouteChangeEvent):
        """
        Handle a route change event.

        Args:
            route_event (ft.RouteChangeEvent): The route change event.
        """
        self.root.views.clear()
        if route_event.route in self.pages.keys():
            self.root.views.append(self.pages[route_event.route])
        self.root.update()

    def get_view(self) -> ft.View:
        return ft.View()

    def update_view_state(self,event=None):
        """
        Set the state of the view.

        Args:
            event: An optional event to trigger the state change.
        """
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
        self.update_view_state()

    def on_window_event(self, e:ft.ControlEvent):
        pass
