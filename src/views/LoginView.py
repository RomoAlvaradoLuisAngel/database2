import flet as ft

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(label="Correo Electronico", width = 150, border_radius=10)
    pass_input = ft.TextField(label="Constraseña", password=True, can_reveal_password=True, width=150, border_radius=10)
    
    def login_click(e):
        
    
    return ft.View("/", [
        ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor = ft.Colors.BLUE_GREY_900, color="white"),
        ft.Column([
            ft.Icon(ft.Icons.LOCK_PERSON, size = 50, color=ft.Colors.BLUE),
            ft.Text("Acceso al sistema", size=24, weight="bold"),
            email_input,
            pass_input,
            ft.ElevatedButton("Entrar", on_click=login_click, width=350),
            ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
    ])
    