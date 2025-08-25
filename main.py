from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.v1.marca_router import router as marca_router
from app.core.middleware import LoggingMiddleware
from app.core.exception_handler import (
    http_exception_handler,
    generic_exception_handler,
)

# Inicializamos la aplicación
app = FastAPI(
    title="API de Marcas",
    description="API para gestionar marcas con FastAPI, SQLAlchemy y Alembic",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración de CORS 
origins = [
    "http://localhost",
    "http://localhost:8000",    
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "https://frontend-prueba-iota.vercel.app"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 Agregar middleware de logging
app.add_middleware(LoggingMiddleware)

# 👉 Manejo centralizado de errores
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return await http_exception_handler(request, exc)

@app.exception_handler(Exception)
async def custom_generic_exception_handler(request: Request, exc: Exception):
    return await generic_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": "Validation Error", "details": exc.errors()},
    )

# Registrar routers
app.include_router(marca_router)

# Ruta raíz para verificar que la API está viva
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Marcas 🚀"}
