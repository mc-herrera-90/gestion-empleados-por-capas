from aplicacion.reglas_empleado import ReglasEmpleado
from persistencia.dao.proyecto_dao import ProyectoDAO
from presentacion.utilidades import pedir_opcion_segura, mostrar_mensaje_flush
from aplicacion.reglas_login import ReglasLogin
from persistencia.dao.departamento_dao import DepartamentoDAO
from persistencia.dao.empleado_dao import EmpleadoDAO
from aplicacion.reglas_departamento import ReglasDepartamento
from presentacion.menu_departamento import MenuDepartamento
from presentacion.menu_empleado import MenuEmpleado
from pwinput import pwinput


class MenuPrincipal:

    def __init__(self):

        print("1. Ingresar al sistema")
        print("2. Salir")

        opcion = pedir_opcion_segura("Seleccione una opción: ", [1, 2])

        if opcion == 1:
            self.iniciar_sesion()
        else:
            mostrar_mensaje_flush(borde=True)
            exit()

    def pedir_credenciales(self):
        print("[ INICIO DE SESIÓN ]")
        u = input("Usuario Administrador de Ecotech: ")
        p = pwinput("Contraseña: ", "*")
        return u, p

    def iniciar_sesion(self):
        login = ReglasLogin()
        self.conexion = login.iniciar(self.pedir_credenciales)
        print("Accediendo al sistema...")
        self.mostrar_opciones()

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

            if opcion == 2:
                dao = DepartamentoDAO(self.conexion)
                reglas = ReglasDepartamento(dao)
                menu = MenuDepartamento(reglas)
                menu.mostrar_opciones()

            elif opcion == 4:
                empleado_dao = EmpleadoDAO(self.conexion)
                departamento_dao = DepartamentoDAO(self.conexion)
                proyecto_dao = ProyectoDAO(self.conexion)
                reglas = ReglasEmpleado(empleado_dao, departamento_dao, proyecto_dao)
                menu = MenuEmpleado()
                menu.mostrar_opciones()
            elif opcion == 0:
                mostrar_mensaje_flush(borde=True)
                break

        exit()
