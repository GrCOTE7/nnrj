import flet as ft


class HomeView(ft.View):
    def __init__(self, page: ft.Page, controller):
        super().__init__(route="/", bgcolor="#07112E")
        self.controller = controller
        print(controller.version)
        self._build()

    def _build(self):
        self.controls = [
            ft.Text("Home"),
            ft.Text(f"Version: {self.controller.version}"),
        ]
