import flet as ft


class OnboardingView(ft.View):
    def __init__(self, page: ft.Page, controller):
        super().__init__(route="/", bgcolor="#07112E")
        self.controller = controller
        # print(controller.version)
        self._build()

    def _build(self):
        self.controls = [
            ft.Container(
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=24,
                    controls=[
                        ft.Text(
                            "Up U!",
                            size=54,
                            weight=ft.FontWeight.BOLD,
                            color="#00FF6A",
                        ),
                        ft.Text(
                            f"v {self.controller.version}",
                            size=12,
                            color="#FFFFFF",
                            text_align=ft.TextAlign.CENTER,
                            margin=ft.Margin.only(top=-42, left=20),
                        ),
                        ft.Text(
                            "Build new habits, boost your energy!",
                            size=16,
                            color="#FFFFFF",
                            text_align=ft.TextAlign.CENTER,
                            margin=ft.Margin.only(top=-20),
                        ),
                        ft.Button(
                            "Live Better Now!",
                            on_click=lambda _: self.controller.go_to("/habits"),
                            style=ft.ButtonStyle(
                                mouse_cursor=ft.MouseCursor.CLICK,
                                bgcolor="#00FF6A",
                                color="#07112E",
                                text_style=ft.TextStyle(
                                    weight=ft.FontWeight.BOLD, size=18
                                ),
                                shape=ft.RoundedRectangleBorder(radius=7),
                                padding=ft.Padding.symmetric(
                                    horizontal=21, vertical=13
                                ),
                            ),
                        ),
                    ],
                ),
                alignment=ft.Alignment.CENTER,
            )
        ]
