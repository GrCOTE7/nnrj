import flet as ft


class HabitHistoryView(ft.View):
    def __init__(self, page: ft.Page, app_controller):
        super().__init__(route="/history", bgcolor="#07112E")
        self.app_controller = app_controller
        self._build()

    def _build(self):
        # TODO: implémenter l'historique
        self.controls = [
            ft.AppBar(title=ft.Text("History"), bgcolor="#07112E"),
            ft.Text("History — coming soon", color="#FFFFFF"),
        ]
