from typing import Container

import flet as fl
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    ElevatedButton, FilledButton, FilledTonalButton
import datetime as dt

from flet.controls.border_radius import horizontal

dt_now = dt.datetime.now()


def main(page: fl.Page):
    # configurações
    page.title = "APP"
    page.theme_mode = ThemeMode.DARK  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        t1.value = F"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    def verificar_num():
        num1 = int(input_numero.value)
        print(f'asd {num1}')
        try:
            if num1 % 2 == 0:
                t2.value = f'O Numero: {num1} é Par'
                page.update()
            else:
                t2.value = f'O Numero: {num1} é Impar'
                page.update()
        except Exception as e:
            t2.value = f'Apenas Numeros'
            page.update()

    def verificar_idade():
        idade1 = int(input_idade.value)
        i1 = 2026 - idade1
        if i1 > 17:
            t3.value = f"Maior Idade"
            page.update()
        elif i1 <= 17:
            t3.value = f"Menor Idade"
            page.update()

    def verificar_data():
        data_c = dt.datetime.strptime(input_data.value, "%d/%m/%Y")
        d1 = data_c.date()
        i2 = dt_now.now().year - d1.year
        if i2 > 17:
            t3.value = f"Maior Idade"
        elif i2 <= 17:
            t3.value = f"Menor Idade"

    # Componentes
    t1 = Text()
    input_nome = TextField(label="Digite o nome:",border_radius=10)
    input_sobrenome = TextField(label="Digite o sobrenome:",border_radius=10)
    btn_salvar = ElevatedButton("Salvar", on_click=salvar_nome)

    t2 = Text()
    input_numero = TextField(label="Digite um numero:", hint_text="Verifique se é Par ou Impar",border_radius=10)
    btn_par_impar = ElevatedButton("Identificar", on_click=verificar_num)

    t3 = Text()
    input_idade = TextField(label="Digite Ano de nacimento:",border_radius=10)
    input_data = TextField(label="Digite a Data de nacimento:",border_radius=10)
    btn_salvar_ano = ElevatedButton("Calcular Idade", on_click=verificar_idade)
    btn_salvar_data = ElevatedButton("Calcular Data", on_click=verificar_data)

    # Construção da tela
    page.add(
        Column(
            [
                Container(
                    Column(
                        [
                            Text('Atividade 1', weight=FontWeight.BOLD, size=24),
                            input_nome,
                            input_sobrenome,
                            btn_salvar,
                            t1,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.BLUE_800,
                    padding=10,
                    border_radius=15,
                    width=400,
                ),
                Container(
                    Column(
                        [
                            Text('Atividade 2', weight=FontWeight.BOLD, size=24),
                            input_numero,
                            btn_par_impar,
                            t2
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    bgcolor=Colors.BLUE_600,
                    padding=10,
                    border_radius=15,
                    width=400,
                ),
                Container(
                    Column(
                        [
                            Text('Atividade 3', weight=FontWeight.BOLD, size=24),
                            input_idade,
                            btn_salvar_ano,

                            input_data,
                            btn_salvar_data,
                            t3
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    bgcolor=Colors.BLUE_400,
                    padding=10,
                    border_radius=15,
                    width=400,
                ),

            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    )


fl.run(main)
