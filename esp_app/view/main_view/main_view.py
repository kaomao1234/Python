import flet as ft
from view.base_view import BaseView
from viewmodel import MainViewModel


class MainView(BaseView):
    def __init__(self, root: ft.Page, route, view_model: MainViewModel):
        self.view_model = view_model
        self.text = ""
        self.recieve_text = ""
        self.view_model.add_serial_listener(self.on_triger_message)
        super().__init__(root, route)

    def on_click(self, e):
        self.view_model.serial_api.write(self.text)
        self.update_view_state()

    def on_textfield_change(self, e):
        self.text = e.control.value

    def on_triger_message(self):
        self.recieve_text = f"Serial := {self.view_model.serial_read()}"
        self.update_view_state()

    def get_view(self) -> ft.View:
        return ft.View(
            appbar=ft.AppBar(
                bgcolor=ft.colors.BLUE
            ),
            route=self.route,
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(self.recieve_text),
                        ft.TextField(
                            on_change=self.on_textfield_change
                        ),
                        ft.ElevatedButton("send", on_click=self.on_click)
                    ]
                )
            ],
        )
