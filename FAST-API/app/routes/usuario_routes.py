from fastapi import APIRouter, HTTPException
from controllers.usuario_controller import *
from models.usuario_model import usuario

router = APIRouter()

nuevo_usuario = usuarioController()


@router.post("/create_usuario")
async def create_usuario(usuario: Usuario):
    rpta = nuevo_usuario.create_usuaio(usuario)
    return rpta


@router.get("/get_usuario/{usuario_id}",response_model=Usuario)
async def get_usuario(usuario_id: int):
    rpta = nuevo_usuario.get_usuario(usuario_id)
    return rpta

@router.get("/get_usuarios/")
async def get_usuarios():
    rpta = nuevo_usuario.get_usuarios()
    return rpta