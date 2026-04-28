import flet as ft


class OnboardingView(ft.View):
    def __init__(self, page: ft.Page, controller):
        super().__init__(route="/", bgcolor="#07112E")
        self.controller = controller
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
                            color="#00C853",
                        ),
                        ft.Text(
                            f"v 0.0.3",
                            size=12,
                            color="#FFFFFF",
                            text_align=ft.TextAlign.CENTER,
                            margin=ft.margin.only(top=-42, left=20)
                        ),
                        ft.Text(
                            "Build new habits, boost your energy!",
                            size=16,
                            color="#FFFFFF",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Button(
                            "Start",
                            on_click=lambda _: self.controller.go_to("/habits"),
                            bgcolor="#00C853",
                            color="#07112E",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                padding=ft.padding.symmetric(
                                    horizontal=40, vertical=14
                                ),
                            ),
                        ),
                    ],
                ),
                alignment=ft.Alignment.CENTER,
            )
        ]
