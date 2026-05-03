import flet as ft

from src.nnrj.controllers.habit_controller import HabitController


class HabitListView(ft.View):
    def __init__(self, page: ft.Page, app_controller):
        super().__init__(route="/habits", bgcolor="#07112E")
        self.app_controller = app_controller
        self.habit_ctrl = HabitController()
        self._build()

    def _build(self):
        # TODO: implémenter la liste des habitudes
        self.controls = [
            ft.AppBar(
                title=ft.TextButton(
                    "My Habits",
                    on_click=lambda _: self.app_controller.go_to("/"),
                ),
                bgcolor="#07112E",
            ),
            ft.Text("Habit list — coming soon", color="#FFFFFF"),
        ]
