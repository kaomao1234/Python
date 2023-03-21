import flet as ft
from views.__init__ import HomeView
from viewmodels.__init__ import HomeViewModel
from util.multiprovider import MultiProvider


class App:
    def __init__(self, app: ft.Page) -> None:
        self.app = app
        self.routes = {
            "/": HomeView(self)
        }
        self.multiprovider = MultiProvider(
            home_viewmodel=HomeViewModel
        )
        self.app.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.app.on_route_change = self.route_change
        self.app.on_view_pop = self.view_pop
        self.build()

    def build(self) -> None:
        self.app.go("/")

    def route_change(self, route):
        self.app.views.clear()
        self.app.views.append(self.routes['/'])
        if (self.app.route in list(self.routes.keys())):
            self.app.views.append(self.routes[self.app.route])
        self.app.update()

    def view_pop(self,*e):
        if len(list(self.app.views)) > 1:
            self.app.views.pop()
            top_view = list(self.routes.keys())[
                (list(self.routes.values()).index(self.app.views[-1]))]
            self.app.go(top_view)
        else:
            self.app.go('/')


if __name__ == "__main__":
    ft.app(target=App)
