from fastapi import FastAPI
from routes.usuario_routes import router as usuario_router
from routes.tipo_pqr_routes import router as tipo_pqr_router
from routes.rol_routes import router as rol_router
from routes.respuesta_routes import router as respuesta_router
from routes.prioridad_routes import router as prioridad_router
from routes.historial_estado_routes import router as historial_router
from routes.pqr_routes import router as pqr_router
from routes.evidencia_routes import router as evidencia_router
from routes.estado_routes import router as estado_router
from routes.departamento_routes import router as departamento_router
from routes.asignacion_responsable_routes import router as asignacion_responsable_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://zany-dollop-97r6rvrq7qq62jx5-5173.app.github.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_router)
app.include_router(tipo_pqr_router)
app.include_router(rol_router)
app.include_router(respuesta_router)
app.include_router(prioridad_router)
app.include_router(historial_router)
app.include_router(pqr_router)
app.include_router(evidencia_router)
app.include_router(estado_router)
app.include_router(departamento_router)
app.include_router(asignacion_responsable_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)