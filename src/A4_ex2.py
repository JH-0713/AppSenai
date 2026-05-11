import asyncio
from typing import Container
import flet as ft
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    ElevatedButton, FilledButton, FilledTonalButton, View, control, Button
import datetime as dt

from api_enderecos import get_endereco


def main(page: ft.Page):
    # configurações
    page.title = "Exemplo de Endereço"
    page.theme_mode = ThemeMode.DARK  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navigation(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def registrar_dado():
        cep = input_cep.value
        num_c1 = input_nc.value

        tem_erro = False
        if cep:
            input_cep.error = None
        else:
            tem_erro = True
            input_cep.error = "Campo Invalido"

        if not tem_erro:
            input_nc.value = ""
            end1 = get_endereco(cep)
            text_cidade.value = end1["localidade"]
            text_uf.value = end1["uf"]
            text_logra.value = end1["logradouro"]
            text_bairro.value = end1["bairro"]

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    ft.AppBar(
                        title="CEP",
                        bgcolor=Colors.AMBER_300,
                    ),
                    input_cep,
                    input_nc,
                    text_cidade,
                    text_uf,
                    text_logra,
                    text_bairro,
                    btn_salvar,

                ]
            )
        )

    # Componentes
    input_cep = TextField(label="Digite seu CEP", on_submit=lambda: registrar_dado())
    input_nc = TextField(label="Digite o Numero da sua casa")

    btn_salvar = Button("Salvar", width=400, on_click=lambda: registrar_dado())

    text_cidade = TextField(label="Cidade", disabled=True,color=Colors.WHITE_70)
    text_uf = TextField(label="Unidade da Federação",disabled=True,color=Colors.WHITE_70)
    text_logra = TextField(label="Rua",disabled=True,color=Colors.WHITE_70)
    text_bairro = TextField(label="Bairro",disabled=True,color=Colors.WHITE_70)


    route_change()

ft.run(main)
