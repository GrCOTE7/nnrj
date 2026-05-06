import flet as ft

from nnrj.views.habit_list_view import HabitListView
from nnrj.views.onboarding_view import OnboardingView
from nnrj.views.home_view import HomeView


class AppController:
    def __init__(self, page: ft.Page, app_name: str, version: str):
        self.page = page
        self.app_name = app_name
        self.version = version
        self._setup()

    def _setup(self):
        self.page.on_route_change = self._route_change
        self._render_route(self.page.route or "/")

    def _route_change(self, e: ft.RouteChangeEvent):
        print(e.route)
        self._render_route(e.route or "/")

    def _render_route(self, raw_route: str):
        self.page.views.clear()
        route = raw_route.split("?")[0]

        print(f"Parsed route: {route}")

        if route == "/":
            self.page.views.append(HomeView(self.page, self))
            # self.page.views.append(OnboardingView(self.page, self))
        elif route == "/onboard":
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
