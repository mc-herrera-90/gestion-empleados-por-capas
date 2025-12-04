from aplicacion.reglas_usuario import ReglasUsuario
from dominio.excepciones import (
    UsuarioNoEncontradoError,
    CredencialesInvalidasError,
    EntradaInvalidaError,
)
from presentacion.utilidades import pedir_opcion_segura


class MenuUsuario:

    def __init__(self):
        self.service = ReglasUsuario()

    def mostrar_opciones(self):
        while True:
            print("\n[ MENÚ DE USUARIOS ]")
            print("1. Crear usuario")
            print("2. Modificar usuario")
            print("3. Cambiar contraseña")
            print("4. Eliminar usuario")
            print("5. Listar usuarios")
            print("0. Volver a menú principal")

            opcion = pedir_opcion_segura("Seleccione una opción: ", [1, 2, 3, 4, 5, 0])

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
                    print("Saliendo del menú de usuarios...")
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")

            except (
                UsuarioNoEncontradoError,
                CredencialesInvalidasError,
                EntradaInvalidaError,
            ) as e:
                print(f"Error: {e}")

            except ValueError:
                print("Error: Debe ingresar un número válido para IDs.")
