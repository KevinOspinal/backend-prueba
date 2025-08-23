from pydantic import BaseModel

class MarcaBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class MarcaCreate(MarcaBase):
    pass

class MarcaUpdate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None

class MarcaResponse(MarcaBase):
    id: int

    class Config:
        from_attributes = True
