#!/bin/bash
set -e

# Función de ayuda
function mostrar_ayuda() {
    echo "Uso: ./tools/run.sh [opciones]"
    echo ""
    echo "Opciones:"
    echo "  -h, --help     Muestra esta ayuda"
    echo ""
    echo "Este script:"
    echo "  1. Configura el entorno virtual (crea venv e instala dependencias)."
    echo "  2. Activa el entorno virtual."
    echo "  3. Verifica método de autenticación de MySQL en Linux (Ubuntu/Debian)."
    echo "  4. Ejecuta la inicialización de la base de datos."
    echo "  5. Desactiva el entorno virtual."
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

# Ejecutar setup del entorno virtual
chmod +x ./tools/setup_venv.sh
./tools/setup_venv.sh

clear
echo ""
echo "SETUP"

# Activar entorno virtual
source ./venv/bin/activate

# Configurar PYTHONPATH para que Python encuentre src/
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"

# Verificación de método de autenticación root en Linux (Ubuntu/Debian)
if [ "$(uname)" = "Linux" ]; then
    if command -v mysql >/dev/null 2>&1; then
        MYSQL_AUTH=$(sudo mysql -u root -e "SELECT plugin FROM mysql.user WHERE user='root';" 2>/dev/null | tail -n1 || echo "")
        if [[ "$MYSQL_AUTH" == "auth_socket" ]]; then
            echo ""
            echo "⚠️  Atención: Tu instalación de MySQL usa auth_socket para el usuario root."
            echo "Esto impedirá que el script de inicialización se conecte con usuario root + contraseña."
            echo ""
            echo "Para solucionarlo, abre la terminal y ejecuta:"
            echo "  sudo mysql"
            echo "  ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'TuContraseña';"
            echo "  FLUSH PRIVILEGES;"
            echo "  exit"
            echo ""
            echo "Luego vuelve a ejecutar: ./tools/run.sh"
            echo ""
            deactivate
            exit 1
        fi
    fi
fi

# Ejecutar inicialización de la base de datos
python -m configuracion.init_db

echo ""
echo "=== Desactivando entorno virtual ==="
deactivate
