import flet as ft

def RegistroView(page: ft.Page, auth_controller):
    nombre_input = ft.TextField(label="Nombre", width = 350, border_radius=10)
    apellido_input = ft.TextField(label="Apellido", width = 350, border_radius=10)    
    email_input = ft.TextField(label="Correo Electronico", width = 350, border_radius=10)
    pass_input = ft.TextField(label="Constraseña", password=True, can_reveal_password=True, width=350, border_radius=10)
    
    def registrarse(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return
        nombre = nombre_input.value
        apellido = apellido_input.value
        email = email_input.value
        contraseña = pass_input.value
        user, msg = auth_controller.login(nombre, apellido, email, contraseña)

        if user:
            page.user_data = user
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
                        
    login_button = ft.ElevatedButton("Crear cuenta", on_click=registrarse, width=350, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.MAIL, color=ft.Colors.WHITE, size=25)))
    registrar_button = ft.ElevatedButton("¿Ya tienes una cuenta?", on_click=lambda _: page.go("/Login"), width=350, bgcolor="green", color = "black", icon=(ft.Icon(ft.Icons.PASSWORD, color=ft.Colors.WHITE, size=25)))
    
    pass_input.on_submit = registrarse
        
    
    return ft.View(
        route = "/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("REGISTRO :)"), bgcolor="cyan", color= "white"),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    registrar_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )