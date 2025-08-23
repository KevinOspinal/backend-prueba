# crea_tablas.py
import asyncio
from app.models.marca import Base
from app.database import engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_tables())
