import flet as ft
from view.baseview import BaseView
from hook import ReferenceNofifier, ReferenceBuilder


class MainView(BaseView):
    def __init__(self, root, route="/"):
        self.option_selected = "Mode"
        self.val = 0
        super().__init__(root, route)

    def on_dropdown_change(self, e: ft.ControlEvent):
        self.option_selected = e.data
        print(self.sized.height)

    def get_view(self):
        print("setState")
        return ft.View(
            route=self.route,
            controls=[
                ft.Row(
                    height=56,
                    controls=[
                        ft.TextButton(
                            "New",
                            on_click=lambda *e: self.update_view_state(
                                lambda: setattr(self, 'val', self.val + 1)),
                            height=self.root.height*0.5,
                            width=150,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(
                                radius=ft.BorderRadius(8, 8, 8, 8)))
                        ),
                        ft.Dropdown(
                            hint_text="Mode",
                            on_change=self.on_dropdown_change,
                            width=200,
                            options=[
                                ft.dropdown.Option("Free-form Snip"),
                                ft.dropdown.Option("Rectangular Snip"),
                                ft.dropdown.Option("Window Snip"),
                                ft.dropdown.Option("Full-screen Snip")
                            ]
                        ),
                        ft.Text(str(self.val))
                    ]
                )
            ]
        )
