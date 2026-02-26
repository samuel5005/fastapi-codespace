from pydantic import BaseModel

class respuesta(BaseModel):
    id_respuesta: int=None
    mensaje: str
    fecha:str
    id_incidencias: str
    id_usuario:str
