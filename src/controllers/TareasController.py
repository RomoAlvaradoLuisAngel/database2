from models.TareaModel import TareaModel

class TareaController:
    def __init__(self):
        self.model = TareaModel()
            
    def obtener_lista(self, id_usuario):
        return [
            {
                "titulo": "Tarea de Prueba 1",
                "descripcion": "Esta es una tarea simulada",
                "prioridad": "Alta",
                "estado": "Pendiente"
            },
            {
                "titulo": "Tarea de Prueba 2",
                "descripcion": "Flet funcionando sin base de datos",
                "prioridad": "Baja",
                "estado": "Completada"
            }
        ]
    
    def guardar_nueva(self, id_usuario, titulo, desc, prio, clas):
        if not titulo:
            return False, "El titulo es obligatorio"
        
        self.model.crear(id_usuario, titulo, desc, prio, clas)
        return True, "Tarea guardada"