from pydantic import BaseModel

class tipo_incidencias(BaseModel):
    id_tipo : int=None
    nombre: str
    incidencias: str
