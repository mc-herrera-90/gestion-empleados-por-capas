from aplicacion.reglas_usuario import ReglasUsuario
from dominio.excepciones import (
    UsuarioNoEncontradoError,
    CredencialesInvalidasError,
    EntradaInvalidaError,
)
from presentacion.utilidades import pedir_opcion_segura
from pwinput import pwinput
from persistencia.dao.usuario_dao import UsuarioDAO
from presentacion.menu_servicio import MenuServicio


class MenuUsuario:

    def __init__(self, reglas_usuario: ReglasUsuario):
        """
        La capa de presentación recibe el servicio ya configurado.
        """
        self.service = reglas_usuario

    def pedir_credenciales_usuario(self):
        print("[ INICIO DE SESIÓN USUARIO ]")
        u = input("Usuario: ")
        p = pwinput("Contraseña: ", "*")
        return u, p

    def iniciar_sesion_usuario(self):
        usuario, password = self.pedir_credenciales_usuario()
        self.service.login(usuario, password)
        print(f"\nBienvenido")
        MenuServicio().mostrar_opciones()

    def mostrar_opciones(self):
        while True:
            print("\n[ MENÚ DE USUARIOS ]")
            print("1. Crear usuario")
            print("2. Modificar usuario")
            print("3. Cambiar contraseña")
            print("4. Eliminar usuario")
            print("5. Listar usuarios")
            print("6. Iniciar sesión como usuario")
            print("0. Volver a menú principal")

            opcion = pedir_opcion_segura(
                "Seleccione una opción: ", [1, 2, 3, 4, 5, 6, 0]
            )

            try:
                if opcion == 1:
                    username = input("Nombre de usuario: ")
                    password = input("Contraseña: ")
                    usuario = self.service.crear_usuario(username, password)
                    print(f"Usuario creado: {usuario}")

                elif opcion == 2:
                    user_id = int(input("ID del usuario a modificar: "))
                    nuevo_username = input("Nuevo nombre de usuario: ")
                    nueva_password = input("Nueva contraseña: ")
                    self.service.modificar_usuario(
                        user_id, nuevo_username, nueva_password
                    )
                    print("Usuario modificado correctamente.")

                elif opcion == 3:
                    username = input("Nombre de usuario: ")
                    nueva_password = input("Nueva contraseña: ")
                    self.service.cambiar_password(username, nueva_password)
                    print("Contraseña cambiada correctamente.")

                elif opcion == 4:
                    user_id = int(input("ID del usuario a eliminar: "))
                    self.service.eliminar_usuario(user_id)
                    print("Usuario eliminado correctamente.")

                elif opcion == 5:
                    usuarios = self.service.listar_usuarios()
                    if usuarios:
                        for u in usuarios:
                            print(f"ID: {u.id}, Username: {u.username}")
                    else:
                        print("No hay usuarios registrados.")

                elif opcion == 6:
                    self.iniciar_sesion_usuario()

                elif opcion == 0:
                    break

            except (
                UsuarioNoEncontradoError,
                CredencialesInvalidasError,
                EntradaInvalidaError,
            ) as e:
                print(f"Error: {e}")

            except ValueError:
                print("Error: Debe ingresar un número válido para IDs.")
