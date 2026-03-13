from fastapi import APIRouter, HTTPException
from controllers.evidencia_controller import *
from models.evidencia_model import Evidencia 

router = APIRouter()

nuevo_evidencia = EvidenciaController()


@router.post("/create_evidencia")
async def create_evidencia(evidencia: Evidencia):
    rpta = nuevo_evidencia.create_evidencia(evidencia)
    return rpta


@router.get("/get_evidencia/{evidencia_id}",response_model=Evidencia)
async def get_evidencia(evidencia_id: int):
    rpta = nuevo_evidencia.get_evidencia(evidencia_id)
    return rpta

@router.get("/get_evidencias/")
async def get_evidencias():
    rpta = nuevo_evidencia.get_evidencias()
    return rpta

@router.put("/update_evidencia/{evidencia_id}")
async def update_evidencia(evidencia_id: int, evidencia: Evidencia):
    return nuevo_evidencia.update_evidencia(evidencia_id, evidencia)

@router.delete("/delete_evidencia/{evidencia_id}")
async def delete_evidencia(evidencia_id: int):
    return nuevo_evidencia.delete_evidencia(evidencia_id)

# Ver todas las evidencias adjuntas a una PQR
@router.get("/get_evidencias_by_pqr/{pqr_id}")
async def get_evidencias_by_pqr(pqr_id: int):
    return nuevo_evidencia.get_evidencias_by_pqr(pqr_id)

# Eliminar todas las evidencias de una PQR de una vez
@router.delete("/delete_evidencias_by_pqr/{pqr_id}")
async def delete_evidencias_by_pqr(pqr_id: int):
    return nuevo_evidencia.delete_evidencias_by_pqr(pqr_id)