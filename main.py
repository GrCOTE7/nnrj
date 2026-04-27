import flet as ft

import tools.gc7 as gc7
import tools.screen_utils as screen_utils

APP_NAME = "NewNRJ"
VERSION = "0.0.1"


def main(page: ft.Page):

    screen_utils.gc7_rules(page, left=1912)  # 1520 ou 1912
    page.title = APP_NAME

    page.add(ft.Text(f"{APP_NAME} - {VERSION}"))
    print(gc7.curr_time(), "-", page.route, "-", page.theme_mode, ">")


ft.run(main)
