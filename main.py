# -*- coding: utf-8 -*-

import flet as ft



def main(page: ft.Page):
    page.title = "Meu app com flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinhamento

    conteiner = ft.Container(
        width=150,
        height=150,
        border=ft.border.all(0.5, ft.colors.GREY_200),
        content=ft.FilledButton("Primeira cor"),
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN_300))
    )
    

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
        bgcolor=ft.colors.GREY,
    )
    senha = ft.TextField(
        label="Digite uma senha",
        password=True,
        can_reveal_password=True,
        bgcolor=ft.colors.GREY,
        #disabled=True, #Para desabilitar
    )

    page.theme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=ft.colors.BLUE,
        primary_container=ft.colors.BLUE_300,
        secondary=ft.colors.GREEN,
        secondary_container=ft.colors.GREEN_300,

        # ...
        ),
    )
    #page.update()


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=diminuir),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=somar),
                ft.ElevatedButton("Clique Aqui!"),
                conteiner,
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        ),
        ft.Row(
            [
                tb,
                
             ],
             alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        ),
        ft.Row(
            [
                senha,
            ],alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        )
        
    )
ft.app(target=main, view=ft.WEB_BROWSER)
# ft.app(target=main)