from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, email, password):
        try:
            #validar datos con el schema
            nuevo_usuario=UsuarioSchema(nombre=nombre, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            #retorna el primer error de validacion encotrado
            return False, e.errors()[0]['msg']
    
    def login(self, email, password):
        try:
            usuario_login = UsuarioLogin(email = email, password = password)
            if UsuarioLogin: 
                success = self.model.iniciar_sesion(usuario_login)
                if success:
                    return True, "Inicio de sesion exitoso"
            else: 
                return False, "Credenciales incorrectas"
                
        except Exception as e:
            print("ERROR EN LOGIN:", e)
            return None, str(e)