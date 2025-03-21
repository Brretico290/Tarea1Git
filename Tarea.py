import flet as ft

def main(page: ft.Page):
    page.title = "Traductor de Frases"
    page.bgcolor = "lightgray"

    frases = {
        "Inglés": "Power comes in response to a need, not a desire. You have to create that need.",
        "Español": "El poder viene en respuesta a una necesidad, no a un deseo. Tienes que crear esa necesidad.",
        "Francés": "Le pouvoir vient en réponse à un besoin, pas à un désir. Vous devez créer ce besoin."
    }

    frase_mostrada = ft.Text(frases["Inglés"], size=16, weight=ft.FontWeight.BOLD)

    def cambiar_frase(e):
        frase_mostrada.value = frases[e.control.value]
        page.update()

    idiomas = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Inglés", label="Inglés"),
            ft.Radio(value="Español", label="Español"),
            ft.Radio(value="Francés", label="Francés")
        ]),
        value="Inglés",
        on_change=cambiar_frase
    )

    page.add(ft.Column([
        frase_mostrada,
        idiomas
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20))

ft.app(target=main)
