import flet as fl
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment


def main(page: fl.Page):
    # configurações
    page.title = "APP"
    page.theme_mode = ThemeMode.LIGHT  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        t1.value = F"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    # Componentes
    t1 = Text()
    input_nome = TextField(label="Digite o nome:")
    input_sobrenome = TextField(label="Digite o sobrenome:")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    # Construção da tela
    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                t1
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    )



fl.app(main)
