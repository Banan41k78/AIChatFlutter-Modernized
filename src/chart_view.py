# src/chart_view.py
from collections import defaultdict

import flet as ft

from storage import load_stats


def chart_view(page: ft.Page) -> ft.Control:
    stats = load_stats()
    by_day: dict[str, float] = defaultdict(float)

    for s in stats:
        day = s["date"][:10]           # YYYY-MM-DD
        by_day[day] += s.get("cost", 0.0)

    days = sorted(by_day.keys())

    if not days:
        return ft.Column([
            ft.Text("Расходы по дням", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Пока нет данных. Отправьте хотя бы один запрос в чате.",
                    color=ft.Colors.GREY),
        ], spacing=15, expand=True)

    max_cost = max(by_day.values()) or 1.0

    bars: list[ft.Control] = []
    for d in days:
        cost = by_day[d]
        height = max(6, int(cost / max_cost * 180))
        bars.append(
            ft.Column(
                [
                    ft.Text(f"${cost:.4f}", size=10),
                    ft.Container(
                        width=26,
                        height=height,
                        bgcolor=ft.Colors.BLUE_400,
                        border_radius=4,
                        tooltip=f"{d}: ${cost:.4f}",
                    ),
                    ft.Text(d[5:], size=10, color=ft.Colors.GREY),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            )
        )

    return ft.Column(
        [
            ft.Text("Расходы по дням", size=20, weight=ft.FontWeight.BOLD),
            ft.Text(f"Всего дней: {len(days)} · Всего: ${sum(by_day.values()):.4f}",
                    size=12, color=ft.Colors.GREY),
            ft.Container(
                content=ft.Row(
                    bars,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    scroll=ft.ScrollMode.AUTO,
                ),
                height=260,
                padding=15,
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                border_radius=12,
            ),
        ],
        spacing=15,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )