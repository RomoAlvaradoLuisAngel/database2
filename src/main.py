import flet as ft
from controllers.UserController import AuthController
from controllers.TareasController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

#uv sync
def main(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            
            page.views.append(LoginView(page, task_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        page.update()
    page.on_route_change = route_change
    page.go("/")
    
def main():
    ft.app(target=start)
    
if __name__ == "__main__":
    main()