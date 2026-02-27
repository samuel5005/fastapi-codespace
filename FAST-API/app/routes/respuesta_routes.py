from fastapi import APIRouter, HTTPException
from controllers.Respuesta_controller import *
from models.Respuesta_model import User

router = APIRouter()

nuevo_respuesta = respuestaController()


@router.post("/create_respuesta")
async def create_respuesta(Respuesta: Respuesta):
    rpta = nuevo_respuesta.create_respuesta(Respuesta)
    return rpta


@router.get("/get_respuesta/{respuesta_id}",response_model=Respuesta)
async def get_respuesta(Respuesta_id: int):
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
