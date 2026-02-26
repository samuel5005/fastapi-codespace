from pydantic import BaseModel

class incidencias(BaseModel):
    id_incidencias: int=None
    fecha: str
    descripcion:str
    id_usuario:str
    id_tipo:str
    id_estado:str
    id_departamento:str
    id_prioridad:str
    departamento:str
    estado:str
    prioridad:str
    tipo_incidencia:str
