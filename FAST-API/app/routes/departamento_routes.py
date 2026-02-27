from fastapi import APIRouter, HTTPException
from controllers.departamento_controller import *
from models.departamento_model import departamento

router = APIRouter()

nuevo_departamento = departamentoController()


@router.post("/create_departamento")
async def create_departamento(departamento: departamento):
    rpta = nuevo_departamento.create_departamento(departamento)
    return rpta


@router.get("/get_departamento/{departamento_id}",response_model=departamento)
async def get_departamento(departamento_id: int):
    rpta = nuevo_departamento.get_departamento(departamento_id)
    return rpta

@router.get("/get_departamentos/")
async def get_departamentos():
    rpta = nuevo_departamento.get_departamentos()
    return rpta

@router.put("/update_departamento/{departamento_id}")
async def update_departamento(departamento_id: int, departamento: Departamento):
    return nuevo_departamento.update_departamento(departamento_id, departamento)

@router.delete("/delete_departamento/{departamento_id}")
async def delete_departamento(departamento_id: int):
    return nuevo_departamento.delete_departamento(departamento_id)