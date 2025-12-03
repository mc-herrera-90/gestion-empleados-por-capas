import logging
from configuracion.entorno import LOGS_DIR

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%d-%m-%Y %H:%M:%S"
)

# Logger BD
logger_bd = logging.getLogger("BD")
handler_bd = logging.FileHandler(LOGS_DIR / "bd.log")
handler_bd.setFormatter(formatter)
logger_bd.addHandler(handler_bd)
logger_bd.setLevel(logging.INFO)

# Logger API
logger_api = logging.getLogger("API")
handler_api = logging.FileHandler(LOGS_DIR / "api.log")
handler_api.setFormatter(formatter)
logger_api.addHandler(handler_api)
logger_api.setLevel(logging.INFO)
