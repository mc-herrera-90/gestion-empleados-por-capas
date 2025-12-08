#!/usr/bin/env bash
set -e

export VENV_DIR="venv"

# Verificar si python3-venv está disponible (aplica por ejemplo en Ubuntu)
if ! python3 -m venv --help >/dev/null 2>&1; then
    echo "⚠️  El paquete python3-venv no está instalado."
    read -p "¿Deseas instalarlo ahora? [y/N]: " RESP
    if [[ "$RESP" =~ ^[Yy]$ ]]; then
        echo "Instalando python3-venv..."
        sudo apt update
        sudo apt install -y python3-venv
    else
        echo "Por favor instala python3-venv manualmente con:"
        echo "    sudo apt install python3-venv"
        exit 1
    fi
fi

echo "🔍 Verificando entorno virtual..."

if [ ! -d "$VENV_DIR" ] || [ ! -f "$VENV_DIR/bin/pip" ]; then
    if [ -d "$VENV_DIR" ]; then
        echo "⚠️  Entorno virtual incompleto o corrupto, se eliminará..."
        rm -rf "$VENV_DIR"
    fi
    echo "⚙️  Creando entorno virtual..."
    python3 -m venv "$VENV_DIR"
fi

echo "📦 Instalando dependencias..."
"$VENV_DIR/bin/pip" install --upgrade pip

if [ -f "requirements.txt" ]; then
    "$VENV_DIR/bin/pip" install -r requirements.txt
fi

echo ""
echo "Para activar el entorno virtual, ejecuta:"
echo "source $VENV_DIR/bin/activate"
