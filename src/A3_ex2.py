import asyncio

import flet as ft
from flet import ThemeMode, Text, TextField, Column, Colors, View, Button, AppBar, ListView, Card, Row, Icon, Padding, \
    Margin, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, Container, FontWeight, CrossAxisAlignment

from flet.controls.material.icons import Icons
from networkx.algorithms.clique import enumerate_all_cliques


# Classe
class Funcionario:
    def __init__(self, nome, id, carga_horaria, funcao, salario):
        self.nome = nome
        self.id = id
        self.carga_horaria = carga_horaria
        self.funcao = funcao
        self.salario = salario


def main(page: ft.Page):
    # configurações
    page.title = "Exercicio 1 - Perfil"
    page.theme_mode = ThemeMode.LIGHT  # ThemeMode.LIGHT ou DARK
    page.window.width = 350
    page.window.height = 700

    lista_dados = []  # ALERTA: GENÉRICO

    # Funções
    ## Navegar
    def navigation(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def detalhes(valor):
        text_nome.value = valor.nome
        text_id.value = valor.id
        text_carga_h.value = valor.carga_horaria
        text_funcao.value = valor.funcao
        text_salario.value = valor.salario

        navigation("/ver_perfil")


    ## Monta lista de ANDROID
    def montar_lista_padrao():
        list_view.controls.clear()
        for i in lista_dados:
            list_view.controls.append(
                ft.ListTile(
                    bgcolor=Colors.GREY_300,
                    leading=Icon(Icons.ACCOUNT_CIRCLE_ROUNDED),
                    title=i.nome,
                    subtitle=i.funcao,
                    trailing=PopupMenuButton(
                        icon=Icon(Icons.MORE_VERT_OUTLINED),
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icon(Icons.REMOVE_RED_EYE_OUTLINED),
                                          on_click=lambda _, user=i: detalhes(user)),

                            PopupMenuItem("Editar", icon=Icon(Icons.EDIT_OUTLINED)),
                            PopupMenuItem("Excluir", icon=Icon(Icons.DELETE_OUTLINED),
                                          on_click=lambda: excluir_dado(i)),
                        ],

                    ),
                )
            )

    ## Adiciona um item na lista
    def registrar_dado():
        nome = input_nome.value.strip()
        id = input_id.value.strip()
        carga_h = input_carga_h.value.strip()
        funcao = input_funcao.value.strip()
        salario = input_salario.value.strip()

        tem_erro = False
        if not nome:
            input_nome.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_nome.error = None

        if not id:
            input_id.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_id.error = None

        if not carga_h:
            input_carga_h.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_carga_h.error = None

        if not funcao:
            input_funcao.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_funcao.error = None

        if not salario:
            input_salario.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_salario.error = None

        if not tem_erro:
            pf1 = Funcionario(nome=nome, id=id, carga_horaria=carga_h, funcao=funcao, salario=salario)
            lista_dados.append(pf1)
            input_nome.value = ""
            input_id.value = ""
            input_carga_h.value = ""
            input_funcao.value = ""
            input_salario.value = ""

            navigation("/listar_perfil")

        montar_lista_padrao()

    ## Excluir um item na lista
    def excluir_dado(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    ## Gerenciar as telas(routes)

    def route_change():
        montar_lista_padrao()
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    ft.AppBar(
                        title="Lista Perfil",
                        bgcolor=Colors.AMBER_300,
                    ),
                    list_view,
                ],
                floating_action_button=ft.FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navigation('/form_cadastro')
                ),
            )
        )
        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        ft.AppBar(
                            title="Cadastro",
                            bgcolor=Colors.AMBER_200,
                        ),
                        input_nome,
                        input_id,
                        input_carga_h,
                        input_funcao,
                        input_salario,
                        btn_salvar,
                    ],
                )
            )

        elif page.route == "/ver_perfil":
            page.views.append(
                View(
                    route="/ver_perfil",
                    controls=[
                        ft.AppBar(
                            title="Detalhes perfil",
                            bgcolor=Colors.AMBER_200,
                        ),
                        Container(
                            Column([
                                Text(text_nome.value, weight=FontWeight.BOLD, size=24),
                                Row([
                                    Icon(ft.Icons.PERM_IDENTITY, color=Colors.AMBER_500, size=15),
                                    Text(text_id.value),
                                ]),
                                Row([
                                    Icon(ft.Icons.ACCESS_TIME, color=Colors.AMBER_500, size=15),
                                    Text(f"{text_carga_h.value}h"),
                                ]),
                                Row([
                                    Icon(ft.Icons.CONTENT_PASTE_SEARCH_OUTLINED, color=Colors.AMBER_500, size=15),
                                    Text(text_funcao.value),
                                ]),
                                Row([
                                    Icon(ft.Icons.ATTACH_MONEY_OUTLINED, color=Colors.AMBER_500, size=15),
                                    Text(f"{text_salario.value}R$"),
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.AMBER_100,
                            padding=10,
                            border_radius=15,
                            width=400,
                        )
                    ],
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    text_nome = Text()
    text_id = Text()
    text_carga_h = Text()
    text_funcao = Text()
    text_salario = Text()

    input_nome = TextField(label='Digite seu Nome', width=400, on_submit=registrar_dado)
    input_id = TextField(label='Digite seu ID', width=400, on_submit=registrar_dado)
    input_carga_h = TextField(label='Digite sua Carga Horaria', width=400, on_submit=registrar_dado)
    input_funcao = TextField(label='Digite sua Função', width=400, on_submit=registrar_dado)
    input_salario = TextField(label='Digite seu Salário', width=400, on_submit=registrar_dado)

    btn_salvar = Button("Salvar", width=400, on_click=lambda: registrar_dado())

    list_view = ListView(height=500, width=400)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


ft.run(main)
