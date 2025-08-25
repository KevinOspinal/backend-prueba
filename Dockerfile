# Imagen base con Python 3.11 slim
FROM python:3.11-slim

# Configuración del directorio de trabajo
WORKDIR /app

# Evita que Python genere archivos .pyc y buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependencias del sistema necesarias para psycopg2 y asyncpg
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia archivos de requirements primero para aprovechar cache
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Expone el puerto de Uvicorn
EXPOSE 8000

# Comando de inicio
CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port $PORT
