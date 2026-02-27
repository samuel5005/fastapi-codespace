from fastapi import APIRouter, HTTPException
from controllers.pqr_controller import *
from models.pqr_model import pqr

router = APIRouter()

nuevo_pqr = pqrController()


@router.post("/create_pqr")
async def create_pqr(pqr: pqr):
    rpta = nuevo_pqr.create_pqr(pqr)
    return rpta


@router.get("/get_pqr/{pqr_id}",response_model=pqr)
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