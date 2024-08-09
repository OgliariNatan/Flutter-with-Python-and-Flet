import flet as ft

def main(page: ft.Page):
    page.title = "Meu app com flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinhamento

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=50)

    def diminuir(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()#atualiza a tela

    def somar(e):
        #print(e)
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()#atualiza a tela
    
    def textbox_changed(e):
        t.value = e.control.value
        page.update()
    
    t = ft.Text()
    tb = ft.TextField(
        label="INFORME O SEU NOME",
        on_change=textbox_changed,
    )

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=diminuir),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=somar),
                ft.ElevatedButton("Click me!"),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        ),
        ft.Row(
            [
                tb,
                t,
             ],
             alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        )
        
    )
#ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)