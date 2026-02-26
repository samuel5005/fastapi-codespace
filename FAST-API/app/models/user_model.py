from pydantic import BaseModel

class usuario(BaseModel):
    id_usuario: int=None
    nombre: str
    cedula:str
    carrera:str
    semestre:str
    cargo:str
    celular:str
    correo:str
    id_rol:str
    rol:str
