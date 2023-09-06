import flet as ft

from widget.view import MainView, HomeView, BaseView


class App:
    def __init__(self, page: ft.Page):
        self.views:list[BaseView] = [
            MainView(page),
        ]
        page.title = "SnippingApp"
        page.go("/")


ft.app(target=App)
