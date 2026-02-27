from fastapi import APIRouter, HTTPException
from controllers.tipo_incidencia_controller import *
from models.tipo_pqr_model import Tipo_pqr

router = APIRouter()

nuevo_tipo_pqr = tipo_pqr_Controller()


@router.post("/create_tipo_pqr")
async def create_tipo_pqr(tipo_pqr: tipo_pqr):
    rpta = nuevo_tipo_pqr.create_tipo_pqr(tipo_pqr)
    return rpta


@router.get("/get_tipo_pqr/{tipo_pqr_id}",response_model=tipo_pqr)
async def get_tipo_pqr(tipo_pqr_id: int):
    rpta = nuevo_tipo_pqr.get_tipo_pqr(tipo_pqr_id)
    return rpta

@router.get("/get_tipo_pqrs/")
async def get_tipo_pqrs():
    rpta = nuevo_tipo_pqr.get_tipo_pqrs()
    return rpta

@router.put("/update_tipo_pqr/{tipo_pqr_id}")
async def update_tipo_pqr(tipo_pqr_id: int, tipo_pqr: Tipo_pqr):
    return nuevo_tipo_pqr.update_tipo_pqr(tipo_pqr_id, tipo_pqr)

@router.delete("/delete_tipo_pqr/{tipo_pqr_id}")
async def delete_tipo_pqr(tipo_pqr_id: int):
    return nuevo_tipo_pqr.delete_tipo_pqr(tipo_pqr_id)