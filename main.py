# -*- coding: utf-8 -*-

import flet as ft
import pyrebase




firebaseConfig = {
  "apiKey": "AIzaSyAn3SvYnMIWxmu4Vt1XorsEUR_E4wqgy80",
  "authDomain": "exemplo-teste-b9336.firebaseapp.com",
  "projectId": "exemplo-teste-b9336",
  "databaseURL": "https:exemplo-teste.firebaseio.com",
  "storageBucket": "exemplo-teste-b9336.appspot.com",
  "messagingSenderId": "1017608586195",
  "appId": "1:1017608586195:web:a10bf65ba85dc32190a526",
  "measurementId": "G-LE71SEWKHS"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()





def main(page: ft.Page):
    page.title = "Meu app com flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinhamento
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_resizable = True
    page.window_width = 650
    page.window_height = 550
    page.padding = 20

    conteiner = ft.Container(
        width=150,
        height=100,
        border=ft.border.all(0.5, ft.colors.GREY_200),
        #content=ft.FilledButton("Primeira cor"),
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
        t.value = None
        print("Entrou func. texbox_changed")
        page.update()
    t = ft.Text()
    
    def entrar_click(e):
        try:
            auth.sign_in_with_email_and_password(t.value, senha.value)
            page.snack_bar = ft.SnackBar( #popup
                content= ft.Text(
                    value= "logado com sucesso",
                ),
                bgcolor=ft.colors.GREEN_400,
                action= "ok",
                duration=3000,
            )
            page.snack_bar.open = True,
            usuario.value = None,
            senha.value = None,
            page.update()
        except:
            page.snack_bar = ft.SnackBar(
                content= ft.Text(
                    value= "Login invalido",
                ),
                bgcolor=ft.colors.RED_400,
                action= "ok",
                duration=3000,
            )
            page.snack_bar.open = True,
            page.update()


    usuario = ft.TextField(
        hint_text= "Email",
        label="Email",
        on_change=textbox_changed,
        bgcolor=ft.colors.GREY_300,
        label_style= ft.TextStyle(
            color= ft.colors.GREY,
        ),
    )
   
    senha = ft.TextField(
        hint_text= "Senha",
        label="Senha",
        password=True,
        can_reveal_password=True,
        bgcolor=ft.colors.GREY_300,
        label_style= ft.TextStyle(
            color= ft.colors.GREY,
        ),
        #disabled=True, #Para desabilitar
    )
    
    entrar = ft.ElevatedButton(
        text='Entrar',
        on_click=entrar_click,
                
    )

    texto_login = ft.Text(
        value="Login",
        size=32,
        weight='bold',
        color=ft.colors.BLUE,
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
                texto_login,
            ],alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        ),
        ft.Row(
            [
                usuario,#login
                
             ],
             alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        ),
        ft.Row(
            [
                senha,
            ],alignment=ft.MainAxisAlignment.CENTER,#Alinhameto da linha
        ),
        ft.Row(
            [
                entrar,
            ],alignment=ft.MainAxisAlignment.CENTER,
        )
        
    )
# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)



#https://www.youtube.com/watch?v=pRZg8brOgX8
#https://blog.marcusoliveiradev.com.br/como-fazer-card-com-html-e-css-responsivo/