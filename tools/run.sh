#!/bin/bash
set -e

HELP=false

# Función de ayuda
function mostrar_ayuda() {
    echo "Uso: ./tools/run.sh [opciones]"
    echo ""
    echo "Opciones:"
    echo "  -h, --help     Muestra esta ayuda"
    echo ""
    echo "Este script:"
    echo "  1. Configura el entorno virtual (instala dependencias)."
    echo "  2. Activa el entorno virtual."
    echo "  3. Ejecuta la inicialización de la base de datos."
    echo "  4. Desactiva el entorno virtual."
}

# Parsear argumentos
for arg in "$@"; do
    case $arg in
        -h|--help)
        mostrar_ayuda
        exit 0
        ;;
    esac
done

chmod +x ./tools/setup_venv.sh
./tools/setup_venv.sh

clear
echo ""
echo "SETUP"
source ./venv/bin/activate

# Configurar PYTHONPATH para que Python encuentre src/
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"

python -m configuracion.init_db

echo ""
echo "=== Desactivando entorno virtual ==="
deactivate

echo ""
echo "✅ Todo listo."
