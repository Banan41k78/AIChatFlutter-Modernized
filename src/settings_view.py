# src/settings_view.py
import flet as ft

from config import PROVIDERS
from storage import load_settings, save_settings
from chat_view import reset_client


def settings_view(page: ft.Page) -> ft.Control:
    settings = load_settings()

    provider_dd = ft.Dropdown(
        label="Провайдер",
        value=settings["provider"],
        options=[ft.dropdown.Option(key=k, text=v["name"]) for k, v in PROVIDERS.items()],
    )
    model_dd = ft.Dropdown(label="Модель", value=settings["model"])
    api_key_tf = ft.TextField(
        label="API-ключ",
        value=settings["api_key"],
        password=True,
        can_reveal_password=True,
        hint_text="sk-...",
    )
    system_tf = ft.TextField(
        label="System prompt",
        value=settings.get("system_prompt", "Ты полезный ассистент."),
        multiline=True,
        min_lines=2,
        max_lines=4,
    )
    status = ft.Text("", color=ft.Colors.GREEN)

    def update_models(e=None):
        models = PROVIDERS[provider_dd.value]["models"]
        model_dd.options = [ft.dropdown.Option(m) for m in models]
        if model_dd.value not in models:
            model_dd.value = models[0]
        page.update()

    def save(e):
        save_settings({
            "provider": provider_dd.value,
            "api_key": api_key_tf.value or "",
            "model": model_dd.value,
            "system_prompt": system_tf.value or "Ты полезный ассистент.",
        })
        reset_client()   # чтобы новый ключ подхватился сразу
        status.value = "Сохранено ✓"
        page.update()

    provider_dd.on_change = update_models
    update_models()

    return ft.Column(
        [
            ft.Text("Настройки провайдера", size=20, weight=ft.FontWeight.BOLD),
            provider_dd,
            model_dd,
            api_key_tf,
            system_tf,
            ft.FilledButton("Сохранить", on_click=save, width=200),
            status,
        ],
        spacing=15,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )