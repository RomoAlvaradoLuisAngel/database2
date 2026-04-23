import flet as ft
USUARIO_VALIDO="admin"
CONTRASEñA_VALIDA = "123456"

def LoginView(page: ft.Page, AuthController):
    email_input = ft.TextField(label="Correo Electronico", width = 350, border_radius=10)
    pass_input = ft.TextField(label="Constraseña", password=True, can_reveal_password=True, width=350, border_radius=10)
    
    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.Snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        def mostrar_dashboard():
            page.clean()  # limpia la pantalla

            page.add(
                ft.AppBar(
                    title=ft.Text("Panel principal"),
                    bgcolor=ft.Colors.BLUE_900,
                    color=ft.Colors.WHITE
                ),
                ft.Column(
                    [
                        ft.Icon(ft.Icons.BOLT, color=ft.Colors.YELLOW, size=100),
                        ft.Text("Bienvenido al sistema."),
                        ft.Text("Has iniciado sesion correctamente.")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            )

            page.update()
        
        
        usuario = email_input.value
        contrasena = pass_input.value
        
        if usuario == USUARIO_VALIDO and contrasena == CONTRASEñA_VALIDA:
            page.user_data = {
                "nombre": "Admin",
                "id_usuario": 1
            }
            page.show_dialog(ft.SnackBar(ft.Text("Inicio de sesion exitoso.")))
            page.go(mostrar_dashboard)
            return
                    
    login_button = ft.ElevatedButton("Entrar", on_click=login_click, width=350, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.MAIL, color=ft.Colors.WHITE, size=25)))
    registrar_button = ft.ElevatedButton("Crear una nueva cuenta", on_click=lambda _: page.go("/registro"), width=350, bgcolor="green", color = "black", icon=(ft.Icon(ft.Icons.PASSWORD, color=ft.Colors.WHITE, size=25)))
    
    pass_input.on_submit = login_click
        
    
    return ft.View(
        route = "/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("SIGE - Login - Cuando va a ganar el cruz azul bebe"), bgcolor="green", color= "white"),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    registrar_button,
                    ft.TextButton("Se te olvido a contraseña?", on_click=lambda _: page.go("/registro"))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )