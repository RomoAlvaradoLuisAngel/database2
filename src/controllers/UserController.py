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
            conn = self.model.db.get_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM usuario WHERE email=%s AND password=%s"
            cursor.execute(query, (email, password))

            user = cursor.fetchone()

            cursor.close()
            conn.close()

            if user:
                return user, "Login correcto"
            else:
                return None, "Credenciales incorrectas"

        except Exception as e:
            print("ERROR EN LOGIN:", e)  # 👈 ESTO ES CLAVE
            return None, str(e)