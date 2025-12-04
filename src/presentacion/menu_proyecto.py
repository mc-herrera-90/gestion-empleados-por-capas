from presentacion.menu import Menu


class MenuProyecto(Menu):

    def __init__(self):
        super().__init__(
            titulo="Menú de Proyectos",
            opciones=[
                "Agregar Proyecto",
                "Mostrar todos",
                "Buscar por código",
                "Buscar por nombre",
                "Modificar",
                "Eliminar",
            ],
        )

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
