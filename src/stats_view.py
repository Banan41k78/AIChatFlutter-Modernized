# src/stats_view.py
from collections import defaultdict

import flet as ft

from storage import load_stats


def stats_view(page: ft.Page) -> ft.Control:
    stats = load_stats()
    by_model: dict[str, dict] = defaultdict(
        lambda: {"in": 0, "out": 0, "cost": 0.0, "count": 0}
    )

    for s in stats:
        m = s["model"]
        by_model[m]["in"] += s.get("tokens_in", 0)
        by_model[m]["out"] += s.get("tokens_out", 0)
        by_model[m]["cost"] += s.get("cost", 0.0)
        by_model[m]["count"] += 1

    total_tokens = sum(d["in"] + d["out"] for d in by_model.values())
    total_cost = sum(d["cost"] for d in by_model.values())

    rows = [
        ft.DataRow(cells=[
            ft.DataCell(ft.Text(m, size=12)),
            ft.DataCell(ft.Text(str(d["count"]))),
            ft.DataCell(ft.Text(str(d["in"]))),
            ft.DataCell(ft.Text(str(d["out"]))),
            ft.DataCell(ft.Text(f"${d['cost']:.4f}")),
        ])
        for m, d in by_model.items()
    ]

    def card(title: str, value: str) -> ft.Card:
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text(title, size=12, color=ft.Colors.GREY),
                    ft.Text(value, size=22, weight=ft.FontWeight.BOLD),
                ], spacing=4),
                padding=15,
                width=160,
            )
        )

    content: list[ft.Control] = [
        ft.Text("Статистика использования", size=20, weight=ft.FontWeight.BOLD),
        ft.Row([card("Всего токенов", str(total_tokens)),
                card("Потрачено", f"${total_cost:.4f}")]),
    ]

    if rows:
        content.append(
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Модель")),
                    ft.DataColumn(ft.Text("Запросы")),
                    ft.DataColumn(ft.Text("Вход")),
                    ft.DataColumn(ft.Text("Выход")),
                    ft.DataColumn(ft.Text("$")),
                ],
                rows=rows,
            )
        )
    else:
        content.append(ft.Text("Пока нет данных", color=ft.Colors.GREY))

    return ft.Column(content, spacing=15, scroll=ft.ScrollMode.AUTO, expand=True)