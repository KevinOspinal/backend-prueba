# app/core/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# Motor asíncrono
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# SessionLocal será asíncrono
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

# Dependencia para FastAPI
async def get_db():
    async with SessionLocal() as session:
        yield session
