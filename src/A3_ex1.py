import asyncio

import flet as ft
from flet import ThemeMode, Text, TextField, Column, Colors, View, Button, AppBar, ListView, Card, Row, Icon, Padding, \
    Margin, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption
from flet.controls.material.icons import Icons


# Classe
class Perfil:
    def __init__(self, nome, sexo, profissao="Profissão"):
        self.nome = nome
        self.profissao = profissao
        self.sexo = sexo

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


    def definir_img(s1):
        if s1 == "Masculino":
            return Icon(Icons.MAN, color=Colors.BLUE)
        elif s1 == "Feminino":
            return Icon(Icons.WOMAN, color=Colors.PINK)
        else:
            return Icon(Icons.ACCOUNT_CIRCLE_ROUNDED)

    ## Monta lista de ANDROID
    def montar_lista_padrao():
        list_view.controls.clear()
        for i in lista_dados:
            list_view.controls.append(
                ft.ListTile(
                    bgcolor=Colors.GREY_300,
                    leading=definir_img(i.sexo),
                    title=i.nome,
                    subtitle=i.profissao,
                    trailing=PopupMenuButton(
                        icon=Icon(Icons.MORE_VERT_OUTLINED),
                        items=[

                            PopupMenuItem("Ver Detalhes", icon=Icon(Icons.REMOVE_RED_EYE_OUTLINED)),
                            PopupMenuItem("Editar", icon=Icon(Icons.EDIT_OUTLINED)),
                            PopupMenuItem("Excluir", icon=Icon(Icons.DELETE_OUTLINED),
                                          on_click=lambda: excluir_dado(i)),
                        ],

                    ),
                )
            )

    ## Adiciona um item na lista
    def registrar_dado():
        nome = input_nome.value
        profissao = input_profissao.value
        sexo = input_sexo.value

        tem_erro = False
        if not nome:
            input_nome.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_nome.error = None

        if not profissao:
            input_profissao.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_profissao.error = None

        if not sexo:
            input_sexo.error = "Campo Obrigatório"
            tem_erro = True
        else:
            input_sexo.error = None

        if not tem_erro:
            pf1 = Perfil(nome=nome.strip(), profissao=profissao.strip(), sexo=sexo.strip())
            lista_dados.append(pf1)
            input_nome.value = ""
            input_profissao.value = ""
            input_sexo.value = ""
            navigation("/listar_perfil")

        montar_lista_padrao()

    ## Excluir um item na lista
    def excluir_dado(item):
        lista_dados.remove(item)
        montar_lista_padrao()


    ## Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                spacing=15,
                controls=[
                    AppBar(
                        title="Exercicio 1 - Perfil",
                        bgcolor=Colors.AMBER_400,
                    ),
                    Button("Lista padrão Android", on_click=lambda: navigation('/listar_perfil'),width=400,height=50),
                ],
            )

        ),

        if page.route == "/listar_perfil":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/listar_perfil",
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

        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        ft.AppBar(
                            title="Cadastro",
                            bgcolor=Colors.AMBER_200,
                        ),
                        input_nome,
                        input_profissao,
                        input_sexo,
                        btn_salvar,
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
    input_nome = TextField(label='Digite seu Nome', width=400, on_submit=registrar_dado)
    input_profissao = TextField(label='Digite sua Profição', width=400, on_submit=registrar_dado)
    input_sexo = Dropdown(
        label="Sexo",
        options=[
            DropdownOption("Masculino"),
            DropdownOption("Feminino"),
        ],
        width=400,
    )


    btn_salvar = Button("Salvar", width=400, on_click=lambda: registrar_dado())

    list_view = ListView(height=500, width=400)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


ft.run(main)
