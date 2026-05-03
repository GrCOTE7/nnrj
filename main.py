import flet as ft

import src.gc7_tools.gc7 as gc7
import src.gc7_tools.screen_utils as screen_utils
from src.nnrj.controllers.app_controller import AppController

APP_NAME = "Up U!"
VERSION = "0.0.3"


def main(page: ft.Page):
    screen_utils.gc7_rules(page, left=1520)  # 1520 ou 1912
    page.title = f"{APP_NAME} - v{VERSION}"

    AppController(page, APP_NAME, VERSION)

    print(gc7.curr_time(), page.route, ">")


ft.run(main)
