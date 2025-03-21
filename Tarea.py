import flet as ft

def main(page: ft.Page):
    page.title = "Traductor de Frases"
    page.bgcolor = "lightgray"

    frases = {
        "Japones": "Chikara wa yokubōde wanaku hitsuyō-sei ni ōjite umaremasu. Hitsuyō-sei wa jibun de tsukuridasanakereba narimasen.",
        "Español": "El poder viene en respuesta a una necesidad, no a un deseo. Tienes que crear esa necesidad.",
        "Ingles": "Power comes from need, not desire, and need must be created by you."
    }

    frase_mostrada = ft.Text(frases["Japones"], size=16, weight=ft.FontWeight.BOLD)

    def cambiar_frase(e):
        frase_mostrada.value = frases[e.control.value]
        page.update()

    idiomas = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Japones", label="Japones"),
            ft.Radio(value="Español", label="Español"),
            ft.Radio(value="Ingles", label="Ingles")
        ]),
        value="Japones",
        on_change=cambiar_frase
    )

    page.add(ft.Column([
        frase_mostrada,
        idiomas
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20))

ft.app(target=main)
