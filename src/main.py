import flet as ft
from controllers.UserController import AuthController
from controllers.TareasController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

#uv sync
def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
        page.views.clear()
        
        # caso 1: login
        if page.route == "/":
            page.views.append(LoginView(page, task_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        
        #caso de seguridad    
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacia")])
            )
            
        page.update()
        
    page.on_route_change = route_change
    #forzamos la navegacion inicial
    page.go("/")
    
    
def main():
    #ejecucion de la app
    ft.app(target=start)
    
if __name__ == "__main__":
    main()