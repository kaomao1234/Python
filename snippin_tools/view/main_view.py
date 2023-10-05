import flet as ft
from view.baseview import BaseView
from viewmodel import MainViewModel
from hook import ValueNotifier, ValueListenableBuilder
import base64


class MainView(BaseView):
    def __init__(self, root, route="/"):
        self.option_selected = "Mode"
        self.view_model = MainViewModel(listenter=self.update_view_state)
        self.textfield_ref = ft.Ref[ft.TextField]()
        self.focus = False
        super().__init__(root, route)

    def on_dropdown_change(self, e: ft.ControlEvent):
        self.option_selected = e.data
        self.update_view_state()

    def get_view(self):
        return ft.View(
            route=self.route,
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            height=56,
                            controls=[
                                ValueListenableBuilder(
                                    self.use_value_notifier(
                                        lambda: self.sized.height),
                                    builder=lambda value: ft.TextButton(
                                        text="New",
                                        height=value,
                                        width=150,
                                        on_click=self.view_model.on_click,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(
                                                radius=ft.BorderRadius(
                                                    8, 8, 8, 8)
                                            )
                                        )
                                    )
                                ).view,
                                ft.Dropdown(
                                    value=self.option_selected,
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
                            ]
                        ),
                        ft.Image(src_base64=self.view_model.full_screen_capture())
                        # ValueListenableBuilder(
                        #     self.use_value_notifier(lambda: self.sized.height),
                        #     builder=lambda value:ft.Image(
                        #         src_base64=self.view_model.full_screen_capture(),
                        #         # height=value-56,
                        #         # expand=True
                        #     )
                        # ).view
                    ]
                )
            ]
        )
