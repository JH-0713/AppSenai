import asyncio
import flet as ft
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight
from api_endpoints import get_planetas,get_characters


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_personagens():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_characters()

        # item é um apelido para o objeto que esta vindo da api
        for personagem in lista_dados["items"]:
            list_view.controls.append(
                ListTile(
                    leading=Image(src=personagem["image"]),
                    title=Text(personagem["name"],weight=FontWeight.BOLD),
                    subtitle=Text(personagem["race"]),
                )
            )
        # TODO: Montar a lista de personagens do seu jeito, capricha ein

    def montar_lista_planetas():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_planetas()

        # item é um apelido para o objeto que esta vindo da api
        for planeta in lista_dados["items"]:
            list_view.controls.append(
                ListTile(
                    leading=Image(src=planeta["image"],width=65),
                    title=Text(planeta["name"],weight=FontWeight.BOLD),
                    subtitle=Text(f"{planeta["description"]}",overflow=ft.TextOverflow.ELLIPSIS,max_lines=2),
                )
            )

    def define_lista(e):
        # Muda a lista de acordo com o indice do NavigationBar
        return montar_lista_planetas() if e.data == 1 else montar_lista_personagens()

    # Gerenciar as telas(routes)
    def route_change():

        # montar_lista()
        montar_lista_personagens()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    ft.AppBar(
                        title=Text("Dragon Ball Z", weight=FontWeight.BOLD),
                        bgcolor=Colors.ORANGE
                    ),
                    Column([
                        pagelet,
                    ])
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)

    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.MAN, label="Personagens"),
                NavigationBarDestination(icon=Icons.BLUR_ON, label="Planetas"),
            ],
            on_change=define_lista,
        ),
        content=Column([
                    list_view,
                ],
            scroll=ScrollMode.HIDDEN,
            height=500
        ),
        height=600,
    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


ft.run(main)