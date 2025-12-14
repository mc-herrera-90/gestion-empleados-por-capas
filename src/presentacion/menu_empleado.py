from presentacion.menu import Menu
from aplicacion.reglas_empleado import ReglasEmpleado


class MenuEmpleado(Menu):

    def __init__(self, reglas: ReglasEmpleado):
        super().__init__(
            titulo="Menú de Empleados",
            opciones=[
                "Agregar Empleado",
                "Mostrar todos",
                "Buscar por código",
                "Buscar por nombre",
                "Modificar",
                "Eliminar",
            ],
        )
        self.reglas = reglas

    def agregar(self):
        pass

    def mostrarTodos(self):
        pass

    def buscarPorCodigo(self):
        pass

    def buscarPorNombre(self):
        pass

    def modificar(self):
        pass

    def eliminar(self):
        pass
