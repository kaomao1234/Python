from view.baseview import BaseView
import flet as ft


class HomeView(BaseView):
    def __init__(self, root, route="/home"):
        super().__init__(root, route)

    def get_view(self) -> ft.View:
        return ft.View(self.route, [
            ft.AppBar(
                title=ft.Text("Home"),
                center_title=True,
                bgcolor=ft.colors.BLUE
            ),
            ft.ElevatedButton("click", on_click=lambda *e: self.root.go("/"))
        ])
