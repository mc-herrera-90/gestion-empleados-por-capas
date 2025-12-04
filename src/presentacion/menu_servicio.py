from aplicacion.servicios import obtener_tasa_desempleo
from presentacion.utilidades import pedir_opcion_segura, graficar_ascii


class MenuServicio:

    def __init__(self):
        pass

    def mostrar_opciones(self):
        """Muestra el menú de servicios hasta que el usuario salga."""
        while True:
            print("\n[ MENÚ DE SERVICIOS ]")
            print("1. Ver tasa de desempleo")
            print("2. Volver al menú principal")

            opcion = pedir_opcion_segura("Seleccione una opción: ", [1, 2])

            if opcion == 1:
                self._mostrar_tasa_desempleo()
            elif opcion == 2:
                break

    def _mostrar_tasa_desempleo(self):
        serie = obtener_tasa_desempleo()
        graficar_ascii("Tasa de Desempleo", serie)
