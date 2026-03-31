import asyncio
from typing import Container
import flet as ft
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    ElevatedButton, FilledButton, FilledTonalButton, View, control, Button
import datetime as dt


def main(page: ft.Page):
    # configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.LIGHT  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def exibir_msg():
        t1.value = f'Bom dia {input_nome.value}, Tudo Bem?'
        input_nome.value = ""
        navigation("/ver_nome")

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
                    ),
                    Text("Digite seu nome para receber uma mensagem"),
                    input_nome,
                    btn_nomear,
                ],
            )

        )
        if page.route == "/ver_nome":
            page.views.append(
                View(
                    route="/ver_nome",
                    controls=[
                        ft.AppBar(
                            title="Seu Nome:"
                        ),
                        t1
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
    t1 = Text()
    input_nome = TextField(label="Nome: ")
    btn_nomear = OutlinedButton('Salvar',on_click=exibir_msg)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


ft.run(main)
