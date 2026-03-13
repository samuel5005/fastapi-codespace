from fastapi import APIRouter, HTTPException
from controllers.pqr_controller import *
from models.pqr_model import Pqr

router = APIRouter()

nuevo_pqr = PqrController()


@router.post("/create_pqr")
async def create_pqr(pqr: Pqr):
    rpta = nuevo_pqr.create_pqr(pqr)
    return rpta


@router.get("/get_pqr/{pqr_id}",response_model=Pqr)
async def get_pqr(pqr_id: int):
    rpta = nuevo_pqr.get_pqr(pqr_id)
    return rpta

@router.get("/get_pqrs/")
async def get_pqrs():
    rpta = nuevo_pqr.get_pqrs()
    return rpta

@router.put("/update_pqr/{pqr_id}")
async def update_pqr(pqr_id: int, pqr: Pqr):
    return nuevo_pqr.update_pqr(pqr_id, pqr)

@router.delete("/delete_pqr/{pqr_id}")
async def delete_pqr(pqr_id: int):
    return nuevo_pqr.delete_pqr(pqr_id)

# ── RUTAS ADICIONALES ─────────────────────────────────────────────────────────

@router.get("/get_pqrs_by_usuario/{usuario_id}")
async def get_pqrs_by_usuario(usuario_id: int):
    return nuevo_pqr.get_pqrs_by_usuario(usuario_id)

@router.get("/get_pqrs_by_estado/{estado_id}")
async def get_pqrs_by_estado(estado_id: int):
    return nuevo_pqr.get_pqrs_by_estado(estado_id)

@router.patch("/update_estado_pqr/{pqr_id}/{nuevo_estado_id}")
async def update_estado_pqr(pqr_id: int, nuevo_estado_id: int):
    return nuevo_pqr.update_estado_pqr(pqr_id, nuevo_estado_id)

@router.get("/get_pqrs_by_departamento/{departamento_id}")
async def get_pqrs_by_departamento(departamento_id: int):
    return nuevo_pqr.get_pqrs_by_departamento(departamento_id)

@router.get("/get_pqrs_by_prioridad/{prioridad_id}")
async def get_pqrs_by_prioridad(prioridad_id: int):
    return nuevo_pqr.get_pqrs_by_prioridad(prioridad_id)
