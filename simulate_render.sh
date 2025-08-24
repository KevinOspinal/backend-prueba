#!/bin/bash

echo "🔍 Simulación de Render iniciada..."

# 1. Ir al directorio del proyecto
cd "$(dirname "$0")"

# 2. Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv .venv

# 3. Activar entorno virtual
source .venv/bin/activate

# 4. Actualizar pip
echo "⬆️ Actualizando pip..."
pip install --upgrade pip

# 5. Instalar dependencias
echo "📥 Instalando dependencias desde requirements.txt..."
pip install -r requirements.txt

# 6. Simular variables de entorno de Render
echo "🔑 Configurando variables de entorno..."
export DB_USER=postgres
export DB_PASSWORD=
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=marcas_db

# 7. Ejecutar migraciones
echo "🛠 Ejecutando migraciones Alembic..."
alembic upgrade head

# 8. Levantar el servidor para prueba
echo "🚀 Levantando servidor en http://127.0.0.1:8000..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
