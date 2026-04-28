import flet as ft

import tools.gc7 as gc7
import tools.screen_utils as screen_utils
from controllers.app_controller import AppController

APP_NAME = "Up U!"
VERSION = "0.0.3"


def main(page: ft.Page):
    screen_utils.gc7_rules(page, left=1520)  # 1520 ou 1912
    page.title = f"{APP_NAME} - v{VERSION}"

    AppController(page, APP_NAME, VERSION)

    print(gc7.curr_time(), f"- {APP_NAME} - v{VERSION} -", page.route, ">")


ft.run(main)
