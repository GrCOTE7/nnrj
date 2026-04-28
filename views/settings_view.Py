import flet as ft

from controllers.settings_controller import SettingsController


class SettingsView(ft.View):
    def __init__(self, page: ft.Page, app_controller):
        super().__init__(route="/settings", bgcolor="#07112E")
        self.app_controller = app_controller
        self.settings_ctrl = SettingsController(page)
        self._build()

    def _build(self):
        # TODO: implémenter le sélecteur de langue et thème
        self.controls = [
            ft.AppBar(title=ft.Text("Settings"), bgcolor="#07112E"),
            ft.Text("Settings — coming soon", color="#FFFFFF"),
        ]
