from pydantic import BaseModel

class evidencia(BaseModel):
    id_evidencia: int = None
    nombre_archivo: str
    tipo_archivo:str
    url:str
    id_incidencia:str