import flet as fl
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
import datetime as dt

dt_now = dt.datetime.now()
def main(page: fl.Page):
    # configurações
    page.title = "Verificar Idade"
    page.theme_mode = ThemeMode.LIGHT  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def verificar_idade():
        idade1 = int(input_idade.value)
        i1 = 2026 - idade1
        if i1 > 17:
            t1.value = f"Maior Idade"
            page.update()
        elif i1 <= 17:
            t1.value = f"Menor Idade"
            page.update()

    def verificar_idade_2():
        data_c = dt.datetime.strptime(input_data.value, "%d/%m/%Y")
        d1 = data_c.date()
        i2 = dt_now.now().year - d1.year
        if i2 > 17:
            t1.value = f"Maior Idade"
            page.update()
        elif i2 <= 17:
            t1.value = f"Menor Idade"
            page.update()


    # Componentes
    t1 = Text()
    input_idade = TextField(label="Digite Ano de nacimento:")
    input_data = TextField(label="Digite a Data de nacimento:")
    btn_salvar_ano = OutlinedButton("Salvar", on_click=verificar_idade)
    btn_salvar_data = OutlinedButton("Salvar", on_click=verificar_idade_2)

    # Construção da tela
    page.add(
        Column(
            [
                input_idade,
                btn_salvar_ano,

                input_data,
                btn_salvar_data,
                t1
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    )


fl.app(main)
