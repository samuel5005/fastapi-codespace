from fastapi import APIRouter, HTTPException
from controllers.departamento_controller import *
from models.departamento_model import Departamento

router = APIRouter()

nuevo_departamento = DepartamentoController()


@router.post("/create_departamento")
async def create_departamento(departamento: Departamento):
    rpta = nuevo_departamento.create_departamento(departamento)
    return rpta


@router.get("/get_departamento/{departamento_id}",response_model=Departamento)
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

# Ver cuál departamento tiene más PQRs asignadas
@router.get("/get_conteo_pqrs_por_departamento/")
async def get_conteo_pqrs_por_departamento():
    return nuevo_departamento.get_conteo_pqrs_por_departamento()