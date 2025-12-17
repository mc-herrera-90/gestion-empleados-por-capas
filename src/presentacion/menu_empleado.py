from presentacion.menu import Menu
from presentacion.utilidades import pedir_opcion_segura, mostrar_mensaje_flush
from presentacion.validaciones import validar_tipo
from aplicacion.reglas_empleado import ReglasEmpleado


class MenuEmpleado(Menu):

    def __init__(self, reglas: ReglasEmpleado):
        super().__init__(
            titulo="Menú de Empleados",
            opciones=[
                "Agregar empleado",
                "Mostrar todos",
                "Buscar por código",
                "Buscar por nombre o RUT",
                "Modificar",
                "Eliminar",
            ],
        )
        self.reglas = reglas

    # ----------------------------------------------------------------------
    # MENU LOOP
    # ----------------------------------------------------------------------
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
        print("\n[ AGREGAR EMPLEADO ]")

        rut = input("RUT: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo: ")
        direccion = input("Dirección (opcional): ") or None
        telefono = input("Teléfono (opcional): ") or None

        ok, salario = validar_tipo(input("Salario (opcional): "), int)
        salario = salario if ok else None

        ok, depto_id = validar_tipo(input("ID Departamento: "), int)
        if not ok:
            print("❌ El ID del departamento debe ser numérico.")
            return

        entrada_proy = input("ID Proyecto (opcional): ")
        ok, proyecto_id = validar_tipo(entrada_proy, int)
        proyecto_id = proyecto_id if ok else None

        try:
            ok = self.reglas.crear_objeto(
                rut=rut,
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                direccion=direccion,
                telefono=telefono,
                salario=salario,
                departamento_id=depto_id,
                proyecto_id=proyecto_id,
            )

            if ok:
                mostrar_mensaje_flush("Empleado agregado con éxito.")
            else:
                mostrar_mensaje_flush("Error al agregar el empleado.")

        except ValueError as e:
            mostrar_mensaje_flush(str(e))

    # ----------------------------------------------------------------------
    # READ ALL
    # ----------------------------------------------------------------------
    def mostrarTodos(self):
        print("\n[ LISTA DE EMPLEADOS ]")
        empleados = self.reglas.mostrar_todos()

        if not empleados:
            print("No hay empleados registrados.")
            return

        for e in empleados:
            print(
                f"{e.id} | {e.rut} | {e.nombre} {e.apellido} | "
                f"Depto: {e.departamento_id} | Proyecto: {e.proyecto_id}"
            )

    # ----------------------------------------------------------------------
    # READ ONE BY ID
    # ----------------------------------------------------------------------
    def buscarPorCodigo(self):
        print("\n[ BUSCAR EMPLEADO POR ID ]")

        ok, codigo = validar_tipo(input("ID del empleado: "), int)

        if not ok:
            print("❌ Debe ingresar un número válido.")
            return

        empleado = self.reglas.buscar(codigo)

        if empleado is None:
            print("⚠️ No existe un empleado con ese ID.")
            return

        print("\n--- EMPLEADO ENCONTRADO ---")
        self._mostrar_detalle(empleado)

    # ----------------------------------------------------------------------
    # SEARCH BY NAME / RUT
    # ----------------------------------------------------------------------
    def buscarPorNombre(self):
        print("\n[ BUSCAR EMPLEADO POR NOMBRE O RUT ]")
        valor = input("Ingrese nombre, apellido o RUT: ")

        resultado = self.reglas.buscar(valor)

        if not resultado:
            print("No se encontraron coincidencias.")
            return

        if isinstance(resultado, list):
            for e in resultado:
                print(f"{e.id} | {e.rut} | {e.nombre} {e.apellido}")
        else:
            self._mostrar_detalle(resultado)

    # ----------------------------------------------------------------------
    # UPDATE
    # ----------------------------------------------------------------------
    def modificar(self):
        print("\n[ MODIFICAR EMPLEADO ]")

        ok, codigo = validar_tipo(input("ID del empleado a modificar: "), int)
        if not ok:
            print("❌ ID inválido.")
            return

        empleado = self.reglas.buscar(codigo)
        if empleado is None:
            print("No existe un empleado con ese ID.")
            return

        print(f"Nombre actual: {empleado.nombre}")
        nuevo_nombre = input("Nuevo nombre (enter para mantener): ")
        if nuevo_nombre.strip():
            empleado.nombre = nuevo_nombre

        print(f"Apellido actual: {empleado.apellido}")
        nuevo_apellido = input("Nuevo apellido (enter para mantener): ")
        if nuevo_apellido.strip():
            empleado.apellido = nuevo_apellido

        print(f"Correo actual: {empleado.correo}")
        nuevo_correo = input("Nuevo correo (enter para mantener): ")
        if nuevo_correo.strip():
            empleado.correo = nuevo_correo

        ok, nuevo_depto = validar_tipo(
            input("Nuevo ID Departamento (enter para mantener): "), int
        )
        if ok:
            empleado.departamento_id = nuevo_depto

        try:
            ok = self.reglas.modificar(empleado)
            if ok:
                mostrar_mensaje_flush("Empleado modificado correctamente.")
            else:
                mostrar_mensaje_flush("Error al modificar el empleado.")

        except ValueError as e:
            mostrar_mensaje_flush(str(e))

    # ----------------------------------------------------------------------
    # DELETE
    # ----------------------------------------------------------------------
    def eliminar(self):
        print("\n[ ELIMINAR EMPLEADO ]")

        ok, codigo = validar_tipo(input("ID del empleado a eliminar: "), int)
        if not ok:
            mostrar_mensaje_flush("ID inválido.")
            return

        if self.reglas.eliminar(codigo):
            mostrar_mensaje_flush("Empleado eliminado.")
        else:
            mostrar_mensaje_flush("No se pudo eliminar el empleado.")

    # ----------------------------------------------------------------------
    # UTIL
    # ----------------------------------------------------------------------
    def _mostrar_detalle(self, e):
        print(f"ID: {e.id}")
        print(f"RUT: {e.rut}")
        print(f"Nombre: {e.nombre}")
        print(f"Apellido: {e.apellido}")
        print(f"Correo: {e.correo}")
        print(f"Departamento: {e.departamento_id}")
        print(f"Proyecto: {e.proyecto_id}")
        print("")
