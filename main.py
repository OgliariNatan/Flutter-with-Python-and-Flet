import flet as ft

def main(page: ft.Page):
    page.title = "Meu app com flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinhamento

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=50)

    def diminuir(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def somar(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=diminuir),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=somar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        )
    )
#ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)