import asyncio
from typing import Container
import flet as ft
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    ElevatedButton, FilledButton, FilledTonalButton, View, control, Button
import datetime as dt


def main(page: ft.Page):
    # configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navigation(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    ft.AppBar(
                        title="Primeira página",
                        bgcolor=Colors.CYAN_700,
                    ),
                    Button('Ir para Segunda Tela', on_click= lambda: navigation("/segunda_tela"))
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        ft.AppBar(
                            title="Segunda página"
                        )
                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

ft.run(main)
