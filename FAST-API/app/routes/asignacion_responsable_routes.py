from fastapi import APIRouter, HTTPException
from controllers.asignacion_responsable_controller import *
from models.asignacion_responsable_model import Asignacion_responsable

router = APIRouter()

nuevo_asignacion_responsable = Asignacion_responsableController()


@router.post("/create_asignacion_responsable")
async def create_asignacion_responsable(asignacion_responsable: Asignacion_responsable):
    rpta = nuevo_asignacion_responsable.create_asignacion_responsable(asignacion_responsable)
    return rpta


@router.get("/get_asignacion_responsable/{asignacion_responsable_id}",response_model=Asignacion_responsable)
async def get_asignacion_repsonsable(asignacion_responsable_id: int):
    rpta = nuevo_asignacion_responsable.get_asignacion_responsable(asignacion_responsable_id)
    return rpta

@router.get("/get_asignacion_responsables/")
async def get_asignacion_responsables():
    rpta = nuevo_asignacion_responsable.get_asignacion_responsables()
    return rpta

@router.put("/update_asignacion_responsable/{asignacion_responsable_id}")
async def update_asignacion_responsable(asignacion_responsable_id: int, asignacion_responsable: Asignacion_responsable):
    return nuevo_asignacion_responsable.update_asignacion_responsable(asignacion_responsable_id, asignacion_responsable)

@router.delete("/delete_asignacion_responsable/{asignacion_responsable_id}")
async def delete_asignacion_responsable(asignacion_responsable_id: int):
    return nuevo_asignacion_responsable.delete_asignacion_responsable(asignacion_responsable_id)

# Ver todas las PQRs asignadas a un responsable — su bandeja de trabajo
@router.get("/get_asignaciones_by_usuario/{usuario_id}")
async def get_asignaciones_by_usuario(usuario_id: int):
    return nuevo_asignacion_responsable.get_asignaciones_by_usuario(usuario_id)

# Ver quién tiene asignada una PQR específica
@router.get("/get_asignacion_by_pqr/{pqr_id}")
async def get_asignacion_by_pqr(pqr_id: int):
    return nuevo_asignacion_responsable.get_asignacion_by_pqr(pqr_id)
