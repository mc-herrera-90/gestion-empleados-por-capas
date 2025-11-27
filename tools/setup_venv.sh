#!/usr/bin/env bash

set -e

VENV_DIR="venv"

echo "🔍 Verificando entorno virtual..."

if [ ! -d "$VENV_DIR" ]; then
    echo "⚙️  Creando entorno virtual..."
    python3 -m venv $VENV_DIR
else
    echo "✔️ El entorno virtual ya existe"
fi

echo "📦 Instalando dependencias..."
./venv/bin/pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    ./venv/bin/pip install -r requirements.txt
fi

echo "Para activar el entorno virtual, ejecuta:"
echo "source venv/bin/activate"
