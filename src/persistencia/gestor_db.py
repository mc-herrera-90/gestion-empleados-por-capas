from persistencia.conexion import Conexion
import pymysql
from configuracion.entorno import ROOT_PATH, DB_ROOT, DB_ROOT_NAME
import os

class GestorBD(Conexion):
  """
  .. include:: ../documentacion/persistencia/gestor_db.md
  """

  def __init__(self,archivo_esquema: str):
    super().__init__(database=DB_ROOT_NAME)
    self.archivo_esquema = os.path.join(ROOT_PATH,'sql', archivo_esquema)

  def crear_esquema(self):
    try:
      with open(self.archivo_esquema, 'r', encoding='utf-8') as f:
        sql_script = f.read()
      # Aquí necesitamos que la conexión sea con el usuario root
      con = self.conectar(DB_ROOT, DB_ROOT_NAME)
      if con is None:
        return False

      print("Tenemos acceso")

      try:
        sentencias = [s.strip() for s in sql_script.split(";") if s.strip()]

        with con.cursor() as cur:
          for setencia in sentencias:
            if setencia:
              cur.execute(setencia)
              
      except pymysql.MySQLError as e:
        print(f"Error: error creando el cursor {e}")

    except FileNotFoundError as e:
      print(f"Error: no se encontró el archivo {e}")

    except IOError as e:
      print(f"Error: al leer el archivo SQL {e}")


if __name__ == '__main__':
  gdb = GestorBD('schema.sql')
  gdb.crear_esquema()
