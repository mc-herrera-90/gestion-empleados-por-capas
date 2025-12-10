from presentacion.menu import Menu
from presentacion.utilidades import pedir_opcion_segura, mostrar_mensaje_flush
from aplicacion.reglas_departamento import ReglasDepartamento
from presentacion.validaciones import validar_tipo


class MenuDepartamento(Menu):

    def __init__(self, reglas: ReglasDepartamento):
        super().__init__(
            titulo="Menú de Departamento",
            opciones=[
                "Agregar departamento",
                "Mostrar todos",
                "Buscar por código",
                "Buscar por nombre",
                "Modificar",
                "Eliminar",
            ],
        )
        self.reglas = reglas

    def mostrar_opciones(self):
        while True:
            super().mostrar_opciones()
            opcion = pedir_opcion_segura(
                "Seleccione una opción: ", [1, 2, 3, 4, 5, 6, 0]
            )

            if opcion == 1:
                self.agregar()

            elif opcion == 2:
                self.mostrarTodos()

            elif opcion == 3:
                self.buscarPorCodigo()

            elif opcion == 4:
                self.buscarPorNombre()

            elif opcion == 5:
                self.modificar()

            elif opcion == 6:
                self.eliminar()

            elif opcion == 0:
                self.volverMenuPrincipal()
                break

    # ----------------------------------------------------------------------
    # CREATE
    # ----------------------------------------------------------------------
    def agregar(self):
        print("\n[ AGREGAR DEPARTAMENTO ]")
        nombre = input("Nombre: ")
        descripcion = input("Descripción (opcional): ")

        ok = self.reglas.crear_objeto(nombre, descripcion or None)

        if ok:
            mostrar_mensaje_flush("Departamento agregado con éxito.")
        else:
            mostrar_mensaje_flush("Error al agregar el departamento.")

    # ----------------------------------------------------------------------
    # READ ALL
    # ----------------------------------------------------------------------
    def mostrarTodos(self):
        print("\n[ LISTA DE DEPARTAMENTOS ]")
        departamentos = self.reglas.mostrar_todos()

        if not departamentos:
            print("No hay departamentos registrados.")
            return

        for d in departamentos:
            print(f"{d.id} | {d.nombre} | {d.descripcion}")

    # ----------------------------------------------------------------------
    # READ ONE BY ID
    # ----------------------------------------------------------------------

    def buscarPorCodigo(self) -> None:
        print("\n[ BUSCAR DEPARTAMENTO POR ID ]")

        entrada = input("ID del departamento: ")
        ok, codigo = validar_tipo(entrada, int)

        if not ok:
            print("❌ Debe ingresar un número válido.\n")
            return

        depto = self.reglas.buscar(codigo)

        if depto is None:
            print("⚠️ No existe un departamento con ese ID.\n")
        else:
            print("\n--- DEPARTAMENTO ENCONTRADO ---")
            print(f"ID: {depto.id}")
            print(f"Nombre: {depto.nombre}")
            print(f"Descripción: {depto.descripcion}\n")

    # ----------------------------------------------------------------------
    # SEARCH BY NAME
    # ----------------------------------------------------------------------
    def buscarPorNombre(self):
        print("\n[ BUSCAR DEPARTAMENTO POR NOMBRE ]")
        nombre = input("Nombre a buscar: ")

        lista = self.reglas.buscar(nombre)

        if not lista:
            print("No se encontraron coincidencias.")
            return

        for d in lista:
            print(f"{d.id} | {d.nombre} | {d.descripcion}")

    def modificar(self):
        print("\n[ MODIFICAR DEPARTAMENTO ]")
        codigo = pedir_opcion_segura("ID del departamento a modificar: ")

        depto = self.reglas.buscar(codigo)
        if depto is None:
            print("No existe un departamento con ese código.")
            return

        print(f"Nombre actual: {depto.nombre}")
        nuevo_nombre = input("Nuevo nombre (enter para mantener): ")
        if nuevo_nombre.strip():
            depto.nombre = nuevo_nombre

        print(f"Descripción actual: {depto.descripcion}")
        nueva_desc = input("Nueva descripción (enter para mantener): ")
        if nueva_desc.strip():
            depto.descripcion = nueva_desc

        ok = self.reglas.modificar(depto)

        if ok:
            mostrar_mensaje_flush("Departamento modificado correctamente.")
        else:
            mostrar_mensaje_flush("Error al modificar el departamento.")

    def eliminar(self):
        print("\n[ ELIMINAR DEPARTAMENTO ]")

        ok, codigo = validar_tipo(input("ID del departamento a eliminar: "), int)

        if ok:
            self.reglas.eliminar(codigo)
            mostrar_mensaje_flush("Departamento eliminado.")
        else:
            mostrar_mensaje_flush("No se pudo eliminar (¿ID inexistente?).")
