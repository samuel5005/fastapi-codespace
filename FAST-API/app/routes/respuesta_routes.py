from fastapi import APIRouter, HTTPException
from controllers.respuesta_controller import *
from models.respuesta_model import Respuesta

router = APIRouter()

nuevo_respuesta = RespuestaController()


@router.post("/create_respuesta")
async def create_respuesta(Respuesta: Respuesta):
    rpta = nuevo_respuesta.create_respuesta(Respuesta)
    return rpta


@router.get("/get_respuesta/{respuesta_id}",response_model=Respuesta)
async def get_respuesta(respuesta_id: int):
    rpta = nuevo_respuesta.get_respuesta(respuesta_id)
    return rpta

@router.get("/get_respuestas/")
async def get_respuestas():
    rpta = nuevo_respuesta.get_respuestas()
    return rpta

@router.put("/update_respuesta/{respuesta_id}")
async def update_respuesta(respuesta_id: int, respuesta: Respuesta):
    return nuevo_respuesta.update_respuesta(respuesta_id, respuesta)

@router.delete("/delete_respuesta/{respuesta_id}")
async def delete_respuesta(respuesta_id: int):
    return nuevo_respuesta.delete_respuesta(respuesta_id)

# Ver el hilo completo de respuestas de una PQR
@router.get("/get_respuestas_by_pqr/{pqr_id}")
async def get_respuestas_by_pqr(pqr_id: int):
    return nueva_respuesta.get_respuestas_by_pqr(pqr_id)

# Ver todas las respuestas que ha dado un usuario/responsable
@router.get("/get_respuestas_by_usuario/{usuario_id}")
async def get_respuestas_by_usuario(usuario_id: int):
    return nueva_respuesta.get_respuestas_by_usuario(usuario_id)

