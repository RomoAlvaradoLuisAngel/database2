import flet as ft

def DashboardView(page, tarea_controller):
    user = page.session.get("user")
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def refres():
        lista_tareas.controls.clear()
        for t in tareas_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTole(
                            title=ft.Text(t['titulo'], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            trailing=ft.Badge(content=ft.Text(t['estado']), bgcolor=ft.Colors.ORANGE_300)
                        ), padding=10
                    )
                )
            )
        page.update()