import asyncio
from typing import Container
import flet as ft
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    ElevatedButton, FilledButton, FilledTonalButton, View, control, Button, Row, Icon, Icons
import datetime as dt

from flet.controls.border_radius import horizontal


def main(page: ft.Page):
    # configurações
    page.title = "Celular"
    page.theme_mode = ThemeMode.LIGHT  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def cadastrar_c():
        t_nome.value = input_nome.value
        t_cor.value = input_cor.value
        t_arm1.value = input_armazenamento.value
        t_versao.value = input_versao.value
        t_modelo.value = input_modelo.value
        t_sistema.value = input_sistema.value

        t1.value = f'''
        Nome: {t_nome}
        Cor: {t_cor}
        Armazenamento: {t_arm1}GB
        Versão: {t_versao}
        Modelo: {t_modelo}
        Sistema: {t_sistema}'''

        tem_erro = False
        if not input_nome.value:
            tem_erro = True
            input_nome.error = 'Campo obrigatorio!'
        else:
            input_nome.error = None

        if not input_cor.value:
            tem_erro = True
            input_cor.error = 'Campo obrigatorio!'
        else:
            input_cor.error = None

        if not input_armazenamento.value:
            tem_erro = True
            input_armazenamento.error = 'Campo obrigatorio!'
        else:
            input_armazenamento.error = None

        if not input_versao.value:
            tem_erro = True
            input_versao.error = 'Campo obrigatorio!'
        else:
            input_versao.error = None

        if not input_modelo.value:
            tem_erro = True
            input_modelo.error = 'Campo obrigatorio!'
        else:
            input_modelo.error = None

        if not input_sistema.value:
            tem_erro = True
            input_sistema.error = 'Campo obrigatorio!'
        else:
            input_sistema.error = None

        if not tem_erro:
            input_nome.value = ""
            input_cor.value = ""
            input_versao.value = ""
            input_armazenamento.value = ""
            input_modelo.value = ""
            input_sistema.value = ""
            navigation("/ver_funcionario")

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
                    ft.AppBar(),
                    Text("Digite os seus dados:"),
                    input_nome,
                    input_cor,
                    input_armazenamento,
                    input_versao,
                    input_modelo,
                    input_sistema,
                    btn_salvar,
                ],
            )

        )
        if page.route == "/ver_funcionario":
            page.views.append(
                View(
                    route="/ver_funcionario",
                    controls=[
                        ft.AppBar(
                        ),
                        Container(
                            Column([
                                Text(t_nome.value, weight=FontWeight.BOLD, size=24),
                                Row([
                                    Icon(Icons.COLOR_LENS, color=Colors.PURPLE_200,size=15),
                                    t_cor,
                                ]),
                                Row([
                                    Icon(Icons.ALL_INBOX, color=Colors.PURPLE_300,size=15),
                                    t_arm1,
                                ]),
                                Row([
                                    Icon(Icons.ACCOUNT_TREE, color=Colors.PURPLE_400,size=15),
                                    t_versao,
                                ]),
                                Row([
                                    Icon(Icons.AOD, color=Colors.PURPLE_500,size=15),
                                    t_modelo,
                                ]),
                                Row([
                                    Icon(Icons.LANGUAGE,color=Colors.PURPLE_600,size=15),
                                    t_sistema,
                                ]),

                            ],
                            horizontal_alignment=CrossAxisAlignment.CENTER,

                            ),
                            bgcolor=Colors.CYAN_300,
                            padding=10,
                            border_radius=15,
                            width=400,
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
    t1 = Text()
    t_nome = Text()
    t_cor = Text()
    t_arm1 = Text()
    t_versao = Text()
    t_modelo = Text()
    t_sistema = Text()

    input_nome = TextField(label="Defina seu Nome do Aparelho: ")
    input_cor = TextField(label="Defina sua Cor: ")
    input_armazenamento = TextField(label="Defina o Tamanho do Armazenamento: ")
    input_versao = TextField(label="Defina sua Versão: ")
    input_modelo = TextField(label="Defina seu Modelo: ")
    input_sistema = TextField(label="Defina seu Sistema Operacional: ")

    btn_salvar = OutlinedButton('Salvar', on_click=cadastrar_c)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


ft.run(main)
