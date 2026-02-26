from pydantic import BaseModel

class prioridad(BaseModel):
    id_prioridad: int = None
    nombre: str
    incidencias:str