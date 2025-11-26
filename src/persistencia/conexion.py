import pymysql
from pymysql.connections import Connection
from typing import Optional

class Conexion:
  """
  Clase base para gestionar la conexión a MySQL.

  No solicita credenciales por consola (la UI debe hacerlo).
  La clase solo intenta conectar y devuelve la conexión.
  """
  def __init__(self,
    host: str = "localhost",
    database: str = "ecotech_solutions_company"
  ) -> None:
    self._host = host
    self._database = database

  def conectar(self, user: str, password: str) -> Optional[Connection]:
    """
    Intenta una conexión ÚNICA.
    La capa aplicación decide si reintenta o no.
    """
    try:
      conn = pymysql.connect(
        host=self._host,
        user=user,
        password=password,
        database=self._database
      )
      return conn

    except pymysql.MySQLError as e:
      print(f"Error al conectar: {e}")
      return None

    def desconectar(self, conexion: Connection) -> bool:
        """
        Cierra la conexión abierta.
        """
        if conexion:
            try:
                conexion.close()
                return True
            except pymysql.MySQLError as e:
                print(f"[Conexion] Error al cerrar conexión: {e}")
                return False
        return False
