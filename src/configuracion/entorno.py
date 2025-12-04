"""
entorno.py — Carga de variables de entorno y rutas internas de la aplicación.

Este módulo se encarga de:

- Leer las variables definidas en el archivo `.env`.
- Proveer configuraciones globales para la aplicación, como:
    - Conexión a bases de datos (HOST, DB_NAME, etc.).
    - URLs de APIs externas y si fuera necesario su respectiva API_KEY.
    - Rutas internas importantes (por ejemplo, carpeta de logs).

Todos los valores definidos aquí son de solo lectura y deben ser
importados por otras capas de la aplicación (persistencia, servicios, presentación)
para mantener una configuración centralizada y coherente.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

ROOT_PATH = Path(__file__).resolve().parent.parent

# Cargar .env
load_dotenv(dotenv_path=ROOT_PATH / ".env")

# Base de datos
DB_HOST: str = os.getenv("DB_HOST", "localhost")
DB_ROOT: str = os.getenv("DB_ROOT", "root")
DB_ROOT_PASSWORD: str = os.getenv("DB_ROOT_PASSWORD", "password")
DB_ROOT_NAME: str = os.getenv("DB_ROOT_NAME", "mysql")
DB_USER: str = os.getenv("DB_USER", "administrador")
DB_USER_PASSWORD: str = os.getenv("DB_USER_PASSWORD", "Admin123!")
DB_NAME: str = os.getenv("DB_NAME", "ecotech_solutions_company")

# API
API_URL: str = os.getenv("API_URL", "https://mindicador.cl/api/")

# Rutas internas
LOGS_DIR: Path = ROOT_PATH / "logs"
LOGS_DIR.mkdir(exist_ok=True)
