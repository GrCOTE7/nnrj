import flet as ft

from nnrj.scripts.app import App
from gc7_tools.gc7 import curr_time
from gc7_tools.screen_utils import gc7_rules

from nnrj.controllers.app_controller import AppController

APP_NAME = "Up You! - Habits Tracker"
UpU_VERSION = "0.0.3"


def main(page: ft.Page):

    gc7_rules(page, left=1520)  # 1520 ou 1912
    page.title = f"{APP_NAME} - v{UpU_VERSION}"

    AppController(page, APP_NAME, UpU_VERSION)
    # App(page, UpU_VERSION) # First real used app

    # print(gc7.curr_time(), "-", page.route, "-", page.theme_mode, ">")
    print(curr_time(), "-", page.route, ">")


ft.run(main)
