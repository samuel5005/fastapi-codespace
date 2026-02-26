from pydantic import BaseModel

class estado(BaseModel):
    id_estado: int = None
    nombre: str
    historial_estados:str
    incidencias:str
