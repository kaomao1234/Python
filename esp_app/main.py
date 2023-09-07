import flet as ft
from view import MainView


def app(root: ft.Page):
    MainView(root=root, route="/")
    root.title = "ESPAPP"


ft.app(app)
