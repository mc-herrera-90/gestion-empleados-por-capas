from pwinput import pwinput
from presentacion.utilidades import pedir_opcion_segura, mostrar_mensaje_flush
from presentacion.menu_usuario import MenuUsuario
from presentacion.menu_servicio import MenuServicio


class MenuPrincipal:

    def __init__(self):
        print("1. Ingresar al sistema")
        print("2. Salir")

        opcion = pedir_opcion_segura("Seleccione una opción: ", [1, 2])

        if opcion == 1:
            self.iniciar_sesion()

        elif opcion == 2:
            mostrar_mensaje_flush(borde=True)
            exit()

    def mostrar_opciones(self):
        while True:
            print("\n[ MENÚ PRINCIPAL ]")
            print("1. Menú de Usuarios")
            print("2. Menú de Departamento")
            print("3. Menú de Proyectos")
            print("4. Menú de Empleados")
            print("5. Menú de Servicios")
            print("0. Salir del programa")

            opcion = pedir_opcion_segura("Seleccione una opción: ", [1, 2, 3, 4, 5, 0])

            if opcion == 1:
                menu_usuario = MenuUsuario()
                menu_usuario.mostrar_opciones()

            elif opcion == 2:
                from presentacion.menu_departamento import MenuDepartamento

                menu_departamento = MenuDepartamento()
                menu_departamento.mostrar_opciones()
            elif opcion == 3:
                from presentacion.menu_proyecto import MenuProyecto

                menu_proyecto = MenuProyecto()
                menu_proyecto.mostrar_opciones()
            if opcion == 5:
                menu_servicio = MenuServicio()
                menu_servicio.mostrar_opciones()

            elif opcion == 0:
                mostrar_mensaje_flush(borde=True)
                break
        exit()

    def pedir_credenciales(self):
        print("[ INICIO DE SESIÓN ]")
        u = input("Usuario Administrador: ")
        p = pwinput("Contraseña: ", "*")
        return u, p

    def iniciar_sesion(self):

        from aplicacion.reglas_login import ReglasLogin

        login = ReglasLogin()
        conexion = login.iniciar(self.pedir_credenciales)
        if conexion.open:
            print("Accediendo al sistema..")
            self.mostrar_opciones()
