import flet as fl
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment

def main(page: fl.Page):
    # configurações
    page.title = "Verificar Numero"
    page.theme_mode = ThemeMode.LIGHT  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def verificar_num():
        num1 = int(input_numero.value)
        print(f'asd {num1}')
        try:
            if num1 % 2 == 0:
                t1.value = f'O Numero: {num1} é Par'
                page.update()
            else:
                t1.value = f'O Numero: {num1} é Impar'
                page.update()
        except Exception as e:
            t1.value = f'Apenas Numeros'
            page.update()

    # Componentes
    t1 = Text()
    input_numero = TextField(label="Digite um numero:")
    btn_salvar = OutlinedButton("Salvar", on_click=verificar_num)

    # Construção da tela
    page.add(
        Column(
            [
                input_numero,
                btn_salvar,
                t1
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    )


fl.app(main)
