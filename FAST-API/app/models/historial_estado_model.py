from pydantic import BaseModel
from datetime import date

class Historial_estado(BaseModel):
    id_historial: int=None
    fecha: date
    id_pqrs: int
    id_estado: int
   