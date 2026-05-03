import flet as ft

from src.nnrj.scripts.app import App
import src.gc7_tools.gc7 as gc7
import src.gc7_tools.screen_utils as screen_utils

APP_NAME = "Sport 2026"
SPORT_VERSION = "0.0.2"


def main(page: ft.Page):

    screen_utils.gc7_rules(page, left=1912)  # 1520 ou 1912
    page.title = APP_NAME + " (DEPRÉCIÉ)"

    App(page, SPORT_VERSION)

    print(gc7.curr_time(), "-", page.route, "-", page.theme_mode, ">")


ft.run(main)
