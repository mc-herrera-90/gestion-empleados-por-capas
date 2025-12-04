import warnings

warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL")

from requests import Session
from requests.exceptions import RequestException, Timeout, HTTPError


API_URL = "https://mindicador.cl/api/"
TIMEOUT_SECONDS = 5
USER_AGENT = "ProyectoGestion/1.0 (+https://midominio.cl)"


session = Session()
session.headers.update(
    {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
)


def obtener_indicador(indicador: str = ""):
    url = API_URL + indicador

    try:
        response = session.get(url, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()  # valida códigos 4xx y 5xx

        data = response.json()  # evita fallo si no es JSON
        if not isinstance(data, dict):
            raise ValueError("La API no retornó un JSON válido.")

        return data

    except Timeout:
        print("❌ Error: La solicitud a Mindicador.cl excedió el tiempo de espera.")
    except HTTPError as e:
        print(f"❌ Error HTTP: {e}")
    except ValueError as e:
        print(f"❌ Error interpretando JSON: {e}")
    except RequestException as e:
        print(f"❌ Error de conexión: {e}")

    return None