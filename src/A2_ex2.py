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
    def cadastrar_f():
        t1.value = (f''',
        Dados:
                Nome:  {input_nome.value}
                CPF:  {input_cpf.value}
                E-mail:  {input_email.value}
                Sálario:  {input_salario.value} R$
            ''')
        tem_erro = False
        if not input_nome.value:
            tem_erro = True
            input_nome.error = 'Campo obrigatorio!'
        else:
            input_nome.error = None

        if not input_cpf.value:
            tem_erro = True
            input_cpf.error = 'Campo obrigatorio!'
        else:
            input_cpf.error = None

        if not input_email.value:
            tem_erro = True
            input_email.error = 'Campo obrigatorio!'
        else:
            input_email.error = None

        if not input_salario.value:
            tem_erro = True
            input_salario.error = 'Campo obrigatorio!'
        else:
            input_salario.error = None

        if not tem_erro:
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                    input_cpf,
                    input_email,
                    input_salario,
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
    input_nome = TextField(label="Defina seu Nome: ")
    input_cpf = TextField(label="Defina seu CPF: ")
    input_email = TextField(label="Defina seu Email: ")
    input_salario = TextField(label="Defina seu Sálario: ")
    btn_salvar = OutlinedButton('Salvar',on_click=cadastrar_f)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


ft.run(main)
