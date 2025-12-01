import os
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_ROOT = os.getenv('DB_ROOT', 'root')
DB_ROOT_PASSWORD = os.getenv('DB_ROOT_PASSWORD', 'admin123')
DB_NAME = os.getenv('DB_NAME', 'mysql')