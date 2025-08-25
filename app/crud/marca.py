from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.marca import Marca
from app.schemas.marca import MarcaCreate, MarcaUpdate


async def create_marca(db: AsyncSession, marca: MarcaCreate):
    nueva_marca = Marca(
        nombre=marca.nombre,
        descripcion=marca.descripcion,
        titular=marca.titular,  
        estado=marca.estado     
    )
    db.add(nueva_marca)
    await db.commit()
    await db.refresh(nueva_marca)
    return nueva_marca


async def get_marcas(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Marca).offset(skip).limit(limit))
    return result.scalars().all()


async def get_marca_by_id(db: AsyncSession, marca_id: int):
    result = await db.execute(select(Marca).where(Marca.id == marca_id))
    return result.scalar_one_or_none()


async def update_marca(db: AsyncSession, marca_id: int, datos: MarcaUpdate):
    result = await db.execute(select(Marca).where(Marca.id == marca_id))
    marca = result.scalar_one_or_none()
    if not marca:
        return None
    if datos.nombre:
        marca.nombre = datos.nombre
    if datos.descripcion:
        marca.descripcion = datos.descripcion
    if datos.titular:
        marca.titular = datos.titular   
    if datos.estado:
        marca.estado = datos.estado    
    await db.commit()
    await db.refresh(marca)
    return marca


async def delete_marca(db: AsyncSession, marca_id: int):
    result = await db.execute(select(Marca).where(Marca.id == marca_id))
    marca = result.scalar_one_or_none()
    if not marca:
        return None
    await db.delete(marca)
    await db.commit()
    return marca
