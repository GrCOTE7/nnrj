import flet as ft

from src.nnrj.views.habit_list_view import HabitListView
from src.nnrj.views.onboarding_view import OnboardingView


class AppController:
    def __init__(self, page: ft.Page, app_name: str, version: str):
        self.page = page
        self.app_name = app_name
        self.version = version
        self._setup()

    def _setup(self):
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = "#07112E"
        self.page.on_route_change = self._route_change
        self._render_route(self.page.route or "/")

    def _route_change(self, e: ft.RouteChangeEvent):
        self._render_route(e.route or "/")

    def _render_route(self, raw_route: str):
        self.page.views.clear()
        route = raw_route.split("?")[0]

        if route == "/":
            self.page.views.append(OnboardingView(self.page, self))
        elif route == "/habits":
            self.page.views.append(HabitListView(self.page, self))
        else:
            # Evite un ecran blanc en cas de route inconnue.
            self.page.views.append(OnboardingView(self.page, self))

        self.page.update()

    def go_to(self, route: str):
        if (self.page.route or "/") == route:
            self._render_route(route)
            return
        self.page.run_task(self._push_route_async, route)

    async def _push_route_async(self, route: str):
        await self.page.push_route(route)
