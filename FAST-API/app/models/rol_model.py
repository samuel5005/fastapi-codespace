from pydantic import BaseModel

class rol(BaseModel):
    id_rol: int = None
    nombre_rol: str
    usuarios:str

