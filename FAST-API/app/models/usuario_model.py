from pydantic import BaseModel



class Usuario(BaseModel):
    id_usuario: int=None
    nombre: str
    cedula:str
    carrera:str
    semestre:int
    cargos:str
    celular:str
    correo:str
    id_rol:int
  
