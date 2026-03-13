from fastapi import APIRouter, HTTPException
from controllers.prioridad_controller import *
from models.prioridad_model import Prioridad

router = APIRouter()

nuevo_prioridad = PrioridadController()


@router.post("/create_prioridad")
async def create_prioridad(prioridad: Prioridad):
    rpta = nuevo_prioridad.create_prioridad(prioridad)
    return rpta


@router.get("/get_prioridad/{prioridad_id}",response_model=Prioridad)
async def get_prioridad(prioridad_id: int):
    rpta = nuevo_prioridad.get_prioridad(prioridad_id)
    return rpta

@router.get("/get_prioridades/")
async def get_prioridades():
    rpta = nuevo_prioridad.get_prioridades()
    return rpta

@router.put("/update_prioridad/{prioridad_id}")
async def update_prioridad(prioridad_id: int, prioridad: Prioridad):
    return nuevo_prioridad.update_prioridad(prioridad_id, prioridad)

@router.delete("/delete_prioridad/{prioridad_id}")
async def delete_prioridad(prioridad_id: int):
    return nuevo_prioridad.delete_prioridad(prioridad_id)

# Ver cuántas PQRs hay por cada nivel de prioridad
@router.get("/get_conteo_pqrs_por_prioridad/")
async def get_conteo_pqrs_por_prioridad():
    return nueva_prioridad.get_conteo_pqrs_por_prioridad()
