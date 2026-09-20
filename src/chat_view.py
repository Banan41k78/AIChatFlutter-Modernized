# src/chat_view.py
import flet as ft

from api_client import AIClient
from storage import load_settings

# Клиент живёт между переключениями страниц — сохраняем историю
_client: AIClient | None = None


def get_client() -> AIClient:
    global _client
    if _client is None:
        _client = AIClient(load_settings())
    return _client


def reset_client() -> None:
    """Сбросить клиент — вызываем после смены настроек."""
    global _client
    _client = None


def chat_view(page: ft.Page) -> ft.Control:
    client = get_client()
    settings = load_settings()

    chat_list = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    message_input = ft.TextField(
        hint_text="Напишите сообщение...",
        expand=True,
        multiline=True,
        min_lines=1,
        max_lines=4,
        border_radius=20,
        filled=True,
    )

    async def send_message(e=None):
        text = (message_input.value or "").strip()
        if not text:
            return
        message_input.value = ""
        message_input.disabled = True
        page.update()

        chat_list.controls.append(
            ft.Container(
                content=ft.Text(text, color=ft.Colors.WHITE),
                bgcolor=ft.Colors.BLUE_700,
                padding=10,
                border_radius=15,
                alignment=ft.alignment.center_right,
            )
        )
        page.update()

        thinking = ft.Text("печатает…", italic=True, color=ft.Colors.GREY)
        chat_list.controls.append(thinking)
        page.update()

        try:
            reply = await client.send(text)
            chat_list.controls.remove(thinking)
            chat_list.controls.append(
                ft.Container(
                    content=ft.Text(reply, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.GREY_800,
                    padding=10,
                    border_radius=15,
                    alignment=ft.alignment.center_left,
                )
            )
        except Exception as ex:
            chat_list.controls.remove(thinking)
            chat_list.controls.append(ft.Text(f"Ошибка: {ex}", color=ft.Colors.RED))

        message_input.disabled = False
        page.update()

    message_input.on_submit = send_message
    send_btn = ft.IconButton(
        icon=ft.Icons.SEND,
        icon_color=ft.Colors.BLUE_400,
        on_click=send_message,
    )

    return ft.Column(
        [
            ft.Text(
                f"{settings['provider']} · {settings['model']}",
                size=11,
                color=ft.Colors.GREY,
            ),
            chat_list,
            ft.Row([message_input, send_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ],
        expand=True,
    )