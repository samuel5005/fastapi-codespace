from fastapi import APIRouter, HTTPException
from controllers.estado_controller import *
from models.estado_model import estado

router = APIRouter()

nuevo_estado = estadoController()


@router.post("/create_estado")
async def create_estado(estado: estado):
    rpta = nuevo_estado.create_estado(estado)
    return rpta


@router.get("/get_estado/{estado_id}",response_model=estado)
async def get_estado(estado_id: int):
    rpta = nuevo_estado.get_estado(estado_id)
    return rpta

@router.get("/get_estados/")
async def get_estados():
    rpta = nuevo_estado.get_estados()
    return rpta

@router.put("/update_estado/{estado_id}")
async def update_estado(estado_id: int, estado: Estado):
    return nuevo_estado.update_estado(estado_id, estado)

@router.delete("/delete_estado/{estado_id}")
async def delete_estado(estado_id: int):
    return nuevo_estado.delete_estado(estado_id)

