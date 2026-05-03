import flet as ft


class HabitView(ft.View):
    def __init__(self, page: ft.Page, app_controller, habit_id: int):
        super().__init__(route=f"/habits/{habit_id}", bgcolor="#07112E")
        self.app_controller = app_controller
        self.habit_id = habit_id
        self._build()

    def _build(self):
        # TODO: implémenter le détail d'une habitude
        self.controls = [
            ft.AppBar(title=ft.Text("Habit Detail"), bgcolor="#07112E"),
            ft.Text("Habit detail — coming soon", color="#FFFFFF"),
        ]
