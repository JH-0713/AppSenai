import asyncio

import flet as ft
from flet import ThemeMode, Text, TextField, Column, Colors, View, Button, AppBar, ListView, Card, Row, Icon, Padding, \
    Margin, PopupMenuButton, PopupMenuItem
from flet.controls.material.icons import Icons


def main(page: ft.Page):
    # configurações
    page.title = "Exemplo de Listas"
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

    ## Monta lista de Texto
    def montar_lista_texto():
        list_view.controls.clear()
        for i in lista_dados:
            list_view.controls.append(
                Text(i)
            )

    ## Monta lista de Card
    def montar_lista_card():
        list_view.controls.clear()
        for i in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row(
                        margin=Margin.all(8),
                        controls=[
                            Icon(Icons.PERSON_OUTLINE),
                            Text(i)
                        ],
                    ),
                )
            )

    ## Monta lista de ANDROID
    def montar_lista_padrao():
        list_view.controls.clear()
        for i in lista_dados:
            list_view.controls.append(
                ft.ListTile(
                    leading=Icon(Icons.PERSON_OUTLINE),
                    title=i,
                    subtitle="Subtitulo",
                    trailing=PopupMenuButton(
                        icon=Icon(Icons.MORE_VERT_OUTLINED),
                        items=[
                            PopupMenuItem("Ver Detalhes",icon=Icon(Icons.REMOVE_RED_EYE_OUTLINED)),
                            PopupMenuItem("Editar",icon=Icon(Icons.EDIT_OUTLINED)),
                            PopupMenuItem("Excluir",icon=Icon(Icons.DELETE_OUTLINED), on_click= lambda: excluir_dado(i)),
                        ]
                    ),
                )
            )

    ## Adiciona um item na lista
    def registrar_dado():
        nome = input_nome.value.strip()
        if nome and not nome in lista_dados:
            lista_dados.append(nome)
            input_nome.error = None
            input_nome.value = ""
        elif nome and nome in lista_dados:
            input_nome.error = "Nome já Registrado"
        else:
            input_nome.error = "Campo Obrigatório"

        montar_lista_texto()
        montar_lista_card()
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
                        title="Exemplo de Listas",
                        bgcolor=Colors.AMBER_400,
                    ),
                    Button("Lista de texto",
                           on_click=lambda: navigation('/lista_texto'),width=400,height=50),
                    Button("Lista de card", on_click=lambda: navigation('/lista_card'),width=400,height=50),
                    Button("Lista padrão Android", on_click=lambda: navigation('/lista_padrao'),width=400,height=50),
                ],
            )

        ),

        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        ft.AppBar(
                            title="Lista de Texto",
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

        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        ft.AppBar(
                            title="Lista de Card",
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

        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        ft.AppBar(
                            title="Lista padrão Android",
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

    btn_salvar = Button("Salvar", width=400, on_click=lambda: registrar_dado())

    list_view = ListView(height=500, width=400)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


ft.run(main)
