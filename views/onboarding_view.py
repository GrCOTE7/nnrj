import flet as ft


class OnboardingView(ft.View):
    def __init__(self, page: ft.Page, controller):
        super().__init__(route="/", bgcolor="#07112E")
        self.page = page
        self.controller = controller
        self._build()

    def _build(self):
        self.controls = [
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=24,
                    controls=[
                        ft.Text(
                            "NewNRJ",
                            size=48,
                            weight=ft.FontWeight.BOLD,
                            color="#00C853",
                        ),
                        ft.Text(
                            "Build new habits. Boost your energy.",
                            size=16,
                            color="#FFFFFF",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.ElevatedButton(
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
            )
        ]
