from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.marca import MarcaCreate, MarcaUpdate, MarcaResponse
from app.crud import marca as crud

router = APIRouter(prefix="/marcas", tags=["Marcas"])

# Crear marca
@router.post("/", response_model=MarcaResponse)
async def crear_marca(marca: MarcaCreate, db: AsyncSession = Depends(get_db)):
    nueva_marca = await crud.create_marca(db, marca)
    return nueva_marca

# Listar marcas
@router.get("/", response_model=list[MarcaResponse])
async def listar_marcas(db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 10):
    marcas = await crud.get_marcas(db, skip, limit)
    return marcas

# Obtener marca por ID
@router.get("/{id}", response_model=MarcaResponse)
async def obtener_marca(id: int, db: AsyncSession = Depends(get_db)):
    marca = await crud.get_marca_by_id(db, id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return marca

# Actualizar marca
@router.put("/{id}", response_model=MarcaResponse)
async def actualizar_marca(id: int, datos: MarcaUpdate, db: AsyncSession = Depends(get_db)):
    marca_actualizada = await crud.update_marca(db, id, datos)
    if not marca_actualizada:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return marca_actualizada

# Eliminar marca
@router.delete("/{id}")
async def eliminar_marca(id: int, db: AsyncSession = Depends(get_db)):
    marca = await crud.delete_marca(db, id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return {"message": "Marca eliminada con éxito"}
