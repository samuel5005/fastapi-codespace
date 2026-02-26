from pydantic import BaseModel

class departamento(BaseModel):
    id_departamento: int = None
    nombre: str
    pqrs:str