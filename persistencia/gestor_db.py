from persistencia.conexion import Conexion
import pymysql
from config.variables import BASE_PATH
import os

class GestorBD(Conexion):
  """
  .. include:: ../documentacion/persistencia/gestor_db.md
  """

  def __init__(self,archivo_esquema: str):
    super().__init__()
    self.archivo_esquema = os.path.join(BASE_PATH,'sql', archivo_esquema)

  def crear_esquema(self):
    try:
      with open(self.archivo_esquema, 'r', encoding='utf-8') as f:
        sql_script = f.read()

      con = self.conectar('administrador', 'admin123')
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


    #     try:
    #         with con.cursor() as cursor:
    #             for statement in sql_script.split(";"):
    #                 stmt = statement.strip()
    #                 if stmt:
    #                     cursor.execute(stmt + ";")
    #         print("🎉 Esquema de la base de datos creado exitosamente.")
    #         return True

    #     except pymysql.MySQLError as e:
    #         print(f"❌ Error al ejecutar el script SQL: {e}")
    #         return False

    # except FileNotFoundError:
    #     print(f"❌ No se encontró el archivo: {self.archivo_esquema}")
    #     return False
    # except IOError as e:
    #     print(f"❌ Error al leer el archivo SQL: {e}")
    #     return False

if __name__ == '__main__':
  gdb = GestorBD('schema.sql')
  gdb.crear_esquema()
