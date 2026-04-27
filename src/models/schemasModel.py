from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time
class UsuarioBaseSchema(BaseModel):
    email: EmailStr
    passwrod: str=Field(min_length=8)   
class UsuarioSchema(UsuarioBaseSchema):
    nombre: str = Field(min_length=8, max_length=100) 
class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"