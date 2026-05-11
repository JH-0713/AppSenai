import asyncio
from typing import Container

import flet as ft
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight
from api_endpoints import get_planetas, get_characters, get_transforms


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

    def selecionar_cor(race1):
        if race1 == "Saiyan":
            return Colors.YELLOW
        elif race1 == "Namekian":
            return Colors.GREEN
        elif race1 == "Human":
            return "#FCCECF"
        elif race1 == "Frieza Race":
            return Colors.RED
        elif race1 == "Android":
            return Colors.BLUE
        elif race1 == "Majin":
            return Colors.PINK_200
        elif race1 == "God":
            return Colors.AMBER
        elif race1 == "Angel":
            return Colors.CYAN
        elif race1 == "Jiren Race":
            return Colors.BLACK
        elif race1 == "Unknown":
            return Colors.PURPLE
        elif race1 == "Evil":
            return Colors.RED_ACCENT_700
        elif race1 == "Nucleico benigno":
            return Colors.BLACK_45
        elif race1 == "Nucleico":
            return Colors.BLACK_12

    def montar_lista_personagens():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_characters()

        # item é um apelido para o objeto que esta vindo da api
        for personagem in lista_dados["items"]:
            list_view.controls.append(
                ft.Card(
                    bgcolor=selecionar_cor(personagem["race"]),
                    content=ft.Container(ft.Row(
                        margin=ft.Margin.all(8),
                        spacing=12,
                        controls=[
                            Image(src=personagem["image"], width=85, height=125),
                            Column([
                                ft.Stack(
                                    controls=[
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Name: {personagem['name']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        foreground=ft.Paint(
                                                            color=ft.Colors.BLACK,
                                                            stroke_width=5,
                                                            style=ft.PaintingStyle.STROKE,
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Name: {personagem['name']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        color=Colors.WHITE,
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                ft.Stack(
                                    controls=[
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Raça: {personagem['race']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        foreground=ft.Paint(
                                                            color=ft.Colors.BLACK,
                                                            stroke_width=5,
                                                            style=ft.PaintingStyle.STROKE,
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Raça: {personagem['race']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        color=Colors.WHITE,
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                ft.Stack(
                                    controls=[
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Gênero: {personagem['gender']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        foreground=ft.Paint(
                                                            color=ft.Colors.BLACK,
                                                            stroke_width=5,
                                                            style=ft.PaintingStyle.STROKE,
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Gênero: {personagem['gender']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        color=Colors.WHITE,
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ]),
                            Column([
                                ft.Stack(
                                    controls=[
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(

                                                    text=f"Base: {personagem['ki']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        foreground=ft.Paint(
                                                            color=ft.Colors.BLACK,
                                                            stroke_width=5,
                                                            style=ft.PaintingStyle.STROKE,
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Base: {personagem['ki']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        color="#75DDFF",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                ft.Stack(
                                    controls=[
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(

                                                    text=f"Max: {personagem['maxKi']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        foreground=ft.Paint(
                                                            color=ft.Colors.BLACK,
                                                            stroke_width=5,
                                                            style=ft.PaintingStyle.STROKE,
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ft.Text(
                                            size=12,
                                            spans=[
                                                ft.TextSpan(
                                                    text=f"Max: {personagem['maxKi']}",
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        color="#75DDFF",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ],
                                spacing=15
                            )
                        ],
                    ),
                        on_click=lambda _, id_p=personagem["id"]: monta_detalhes(id_p)
                    )
                )

            )

    def montar_lista_planetas():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_planetas()

        # item é um apelido para o objeto que esta vindo da api
        for planeta in lista_dados["items"]:
            list_view.controls.append(
                ListTile(
                    leading=Image(src=planeta["image"], width=65),
                    title=Text(planeta["name"], weight=FontWeight.BOLD),
                    subtitle=Text(f"{planeta["description"]}", overflow=ft.TextOverflow.ELLIPSIS, max_lines=2),
                )
            )

    def monta_detalhes(id):
        list_view.controls.clear()
        lista_dados = get_transforms(id)
        if len(lista_dados["transformations"]) != 0:
            for personagem in lista_dados["transformations"]:
                list_view.controls.append(
                    ft.Card(
                        content=ft.Container(ft.Row(
                            margin=ft.Margin.all(8),
                            spacing=12,
                            controls=[
                                Image(src=personagem["image"], width=85, height=150),
                                Column([
                                    ft.Stack(
                                        controls=[
                                            ft.Text(
                                                size=12,
                                                spans=[
                                                    ft.TextSpan(
                                                        text=f"Name: {personagem['name']}",
                                                        style=ft.TextStyle(
                                                            weight=ft.FontWeight.BOLD,
                                                            foreground=ft.Paint(
                                                                color=ft.Colors.BLACK,
                                                                stroke_width=5,
                                                                style=ft.PaintingStyle.STROKE,
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            ft.Text(
                                                size=12,
                                                spans=[
                                                    ft.TextSpan(
                                                        text=f"Name: {personagem['name']}",
                                                        style=ft.TextStyle(
                                                            weight=ft.FontWeight.BOLD,
                                                            color=Colors.WHITE,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    ft.Stack(
                                        controls=[
                                            ft.Text(
                                                size=12,
                                                spans=[
                                                    ft.TextSpan(

                                                        text=f"KI: {personagem['ki']}",
                                                        style=ft.TextStyle(
                                                            weight=ft.FontWeight.BOLD,
                                                            foreground=ft.Paint(
                                                                color=ft.Colors.BLACK,
                                                                stroke_width=5,
                                                                style=ft.PaintingStyle.STROKE,
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            ft.Text(
                                                size=12,
                                                spans=[
                                                    ft.TextSpan(
                                                        text=f"KI: {personagem['ki']}",
                                                        style=ft.TextStyle(
                                                            weight=ft.FontWeight.BOLD,
                                                            color="#75DDFF",
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                ],
                                    spacing=15
                                )
                            ],
                        ),
                    )

                )
            )
        else:
            list_view.controls.append(
                ft.Card(
                    content=ft.Container(ft.Row(
                        margin=ft.Margin.all(8),
                        spacing=12,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Text(
                                        size=12,
                                        spans=[
                                            ft.TextSpan(

                                                text=f"Sem Transformações",
                                                style=ft.TextStyle(
                                                    weight=ft.FontWeight.BOLD,
                                                    foreground=ft.Paint(
                                                        color=ft.Colors.BLACK,
                                                        stroke_width=5,
                                                        style=ft.PaintingStyle.STROKE,
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    ft.Text(
                                        size=12,
                                        spans=[
                                            ft.TextSpan(
                                                text=f"Sem Transformações",
                                                style=ft.TextStyle(
                                                    weight=ft.FontWeight.BOLD,
                                                    color="#75DDFF",
                                                ),
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ]

                    )
                    )

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

        if page.route == "/transformacao":
            page.views.append(
                View(
                    route="/transformacao",
                    controls=[
                        ft.AppBar(
                            title="Transformacões",
                            bgcolor=Colors.ORANGE_ACCENT,
                        ),
                        ft.Card(
                            bgcolor=Colors.BLUE,
                            content=ft.Container(ft.Row(
                                margin=ft.Margin.all(8),
                                spacing=12,
                                controls=[]
                            ),
                            )
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
