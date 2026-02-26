from pydantic import BaseModel

class historial_estado(BaseModel):
    id_historial: int = None
    fecha: str
    id_incidencia:str
    id_estado:str
    estado:str
