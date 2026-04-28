import flet as ft


class HabitCheckinView(ft.View):
    def __init__(self, page: ft.Page, app_controller):
        super().__init__(route="/checkin", bgcolor="#07112E")
        self.app_controller = app_controller
        self._build()

    def _build(self):
        # TODO: implémenter l'animation de check-in
        self.controls = [
            ft.AppBar(title=ft.Text("Check-in"), bgcolor="#07112E"),
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                controls=[
                    ft.Text("✓", size=80, color="#00C853"),
                    ft.Text("Great! New energy unlocked.", size=18, color="#FFFFFF"),
                ],
            ),
        ]
