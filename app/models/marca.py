from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(255))
    titular = Column(String(100), nullable=False)   # 👈 nuevo campo
    estado = Column(String(50), nullable=False)     # 👈 nuevo campo
