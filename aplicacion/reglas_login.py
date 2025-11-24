from persistencia.conexion import Conexion

class ReglasLogin:
  """
  .. include:: ../documentacion/aplicacion/reglas_login.md
  """
  def __init__(self):
    self.con = Conexion()

  def iniciar(self, pedir_credenciales_callback):
    intentos = 3

    while intentos > 0:
      usuario, password = pedir_credenciales_callback()

      conexion = self.con.conectar(usuario, password)

      if conexion:
        print("Inicio de sesión exitoso.")
        return conexion

      intentos -= 1
      print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

    print("Se agotaron los intentos. Saliendo del sistema.")
    exit()
