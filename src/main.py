# src/main.py
import flet as ft

from chat_view import chat_view
from settings_view import settings_view
from stats_view import stats_view
from chart_view import chart_view


def main(page: ft.Page):
    page.title = "AI Chat"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    page.window.width = 420
    page.window.height = 800

    body = ft.Container(expand=True)

    def render(index: int):
        if index == 0:
            body.content = chat_view(page)
        elif index == 1:
            body.content = settings_view(page)
        elif index == 2:
            body.content = stats_view(page)
        elif index == 3:
            body.content = chart_view(page)
        page.update()

    nav = ft.NavigationBar(
        selected_index=0,
        on_change=lambda e: render(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                selected_icon=ft.Icons.CHAT_BUBBLE,
                label="Чат",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label="Настройки",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.BAR_CHART_OUTLINED,
                selected_icon=ft.Icons.BAR_CHART,
                label="Статистика",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SHOW_CHART_OUTLINED,
                selected_icon=ft.Icons.SHOW_CHART,
                label="График",
            ),
        ],
    )

    page.add(ft.Column([body, nav], expand=True, spacing=0))
    render(0)


if __name__ == "__main__":
    ft.run(main)