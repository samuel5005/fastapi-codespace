from pydantic import BaseModel
from datetime import date

class Asignacion_responsable(BaseModel):
    id_asignacion: int =None
    id_pqr: int
    id_usuario: int
    fecha_asignacion: date
    
   