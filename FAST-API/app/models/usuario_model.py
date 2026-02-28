from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    id_usuario: Optional[int] =None
    nombre: Optional[str] =None
    cedula: Optional[str] =None
    carrera: Optional[str] =None
    semestre: Optional[int] =None
    cargo: Optional [str] = None
    celular: Optional[str] =None
    correo: Optional[str] =None
    id_rol: Optional[int] =None
  
