from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time
class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str=Field(min_length=8)   
    
class UsuarioSchema(UsuarioLogin):
    nombre: str = Field(min_length=8, max_length=100) 
    

class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"
    
class UsuarioNuevo(BaseModel):
    email: EmailStr
    activo: bool = True
    password: str = Field(min_length=8)
    fecha_registro: datetime = Field(defa)
    ultimo_acceso: date
    nombre: str = Field(min_lenght=3, max_lenght=100)
    apellido: str = Field(min_lenght=3, max_lenght=100)
    telefono: int