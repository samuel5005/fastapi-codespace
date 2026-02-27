from fastapi import APIRouter, HTTPException
from controllers.historial_estado_controller import *
from models.historial_estado_model import historial_estado

router = APIRouter()

nuevo_historial_estado = historial_estado_Controller()


@router.post("/create_historial_estado")
async def create_historial_estado(historial_estado: historial_estado):
    rpta = nuevo_historial_estado.create_historial_estado(historial_estado)
    return rpta


@router.get("/get_historial_estado/{historial_estado_id}",response_model=historial_estado)
async def get_historial_estado(historial_estado_id: int):
    rpta = nuevo_historial_estado.get_historial_estado(historial_estado_id)
    return rpta

@router.get("/get_historial_estados/")
async def get_historial_estados():
    rpta = nuevo_historial_estado.get_historial_estados()
    return rpta

@router.put("/update_historial_estado/{historial_estado_id}")
async def update_historial_estado(historial_estado_id: int, historial_estado: Historial_estado):
    return nuevo_historial_estado.update_historial_estado(historial_estado_id, historial_estado)

@router.delete("/delete_historial_estado/{historial_estado_id}")
async def delete_historial_estado(historial_estado_id: int):
    return nuevo_historial_estado.delete_historial_estado(historial_estado_id)
