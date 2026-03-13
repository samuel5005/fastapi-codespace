from fastapi import APIRouter, HTTPException
from controllers.rol_controller import *
from models.rol_model import Rol

router = APIRouter()

nuevo_rol = RolController()


@router.post("/create_rol")
async def create_rol(rol: Rol):
    rpta = nuevo_rol.create_rol(rol)
    return rpta


@router.get("/get_rol/{rol_id}",response_model=Rol)
async def get_rol(rol_id: int):
    rpta = nuevo_rol.get_rol(rol_id)
    return rpta

@router.get("/get_roles/")
async def get_roles():
    rpta = nuevo_rol.get_roles()
    return rpta

@router.put("/update_rol/{rol_id}")
async def update_rol(rol_id: int, rol: Rol):
    return nuevo_rol.update_rol(rol_id, rol)

@router.delete("/delete_rol/{rol_id}")
async def delete_rol(rol_id: int):
    return nuevo_rol.delete_rol(rol_id)

# Ver cuántos usuarios tiene cada rol
@router.get("/get_conteo_usuarios_por_rol/")
async def get_conteo_usuarios_por_rol():
    return nuevo_rol.get_conteo_usuarios_por_rol()
