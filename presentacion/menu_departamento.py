from presentacion.menu import Menu

class MenuDepartamento(Menu):
    
    def mostrar_opciones(self):
        print("Opciones del Menú de Departamento:")
        print("1. Agregar Departamento")
        print("2. Eliminar Departamento")
        print("3. Listar Departamentos")
        print("4. Volver al Menú Principal")

    def seleccionar_opcion(self, opcion):
        if opcion == 1:
            print("Agregar Departamento seleccionado.")
            # Lógica para agregar departamento
        elif opcion == 2:
            print("Eliminar Departamento seleccionado.")
            # Lógica para eliminar departamento
        elif opcion == 3:
            print("Listar Departamentos seleccionado.")
            # Lógica para listar departamentos
        elif opcion == 4:
            print("Volviendo al Menú Principal.")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")