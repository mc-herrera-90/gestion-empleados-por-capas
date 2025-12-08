from persistencia.conexion import Conexion


class ReglasLogin:

    def __init__(self) -> None:
        pass

    def iniciar(self, pedir_credenciales_callback):
        intentos = 3

        while intentos > 0:
            usuario, password = pedir_credenciales_callback()

            conexion = Conexion(user=usuario, password=password)

            if conexion.abrir():
                print("\nInicio de sesión exitoso.")
                return conexion

            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

        print("Se agotaron los intentos. Saliendo del sistema.")
        exit()
