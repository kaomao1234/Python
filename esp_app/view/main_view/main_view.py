import flet as ft
from view.base_view import BaseView


class MainView(BaseView):
    def __init__(self, root: ft.Page, route):
        super().__init__(root, route)

    def get_view(self) -> ft.View:
        return ft.View(
            appbar=ft.AppBar(
                bgcolor=ft.colors.BLUE
            ),
            route=self.route,
            controls=[

            ],
        )
