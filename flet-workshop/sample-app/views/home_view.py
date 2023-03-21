import flet as ft


class HomeView(ft.View):
    def __init__(self, root):
        super().__init__(
            appbar=ft.AppBar(
                title=ft.Text("Flet app"),
                bgcolor=ft.colors.BLUE_200),
            controls=[
                ft.TextButton("pop", on_click=lambda *e:root.view_pop()),
                ft.TextButton("pop", on_click=lambda *e:root.app.go('/'))

            ]
        )
