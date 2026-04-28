import flet as ft


class HabitCreateView(ft.View):
    def __init__(self, page: ft.Page, app_controller):
        super().__init__(route="/habits/new", bgcolor="#07112E")
        self.page = page
        self.app_controller = app_controller
        self._build()

    def _build(self):
        # TODO: implémenter la création d'habitude
        self.controls = [
            ft.AppBar(title=ft.Text("New Habit"), bgcolor="#07112E"),
            ft.Text("Create habit — coming soon", color="#FFFFFF"),
        ]
