from pydantic import BaseModel
from datetime import date

class asignacion_responsable(BaseModel):
    id_asignacion: Optional[int] =None
    id_pqr: Optional[int] =None
    id_usuario: Optional[int] =None
    fecha: date
   