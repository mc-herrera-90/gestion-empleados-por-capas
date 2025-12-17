from aplicacion.servicios import obtener_tasa_desempleo, obtener_indicador_diario
from presentacion.utilidades import (
    pedir_opcion_segura,
    graficar_ascii,
    mostrar_indicador_diario,
)


class MenuServicio:

    def __init__(self):
        pass

    def mostrar_opciones(self):
        while True:
            print("\n[ MENÚ DE SERVICIOS ]")
            print("1. Ver tasa de desempleo")
            print("2. Ver dólar observado")
            print("3. Ver euro")
            print("4. Ver UF")
            print("5. Ver bitcoin")
            print("0. Volver al menú principal")

            opcion = pedir_opcion_segura("Seleccione una opción: ", [1, 2, 3, 4, 5, 0])

            if opcion == 1:
                serie = obtener_tasa_desempleo()
                graficar_ascii("Tasa de Desempleo", serie)

            elif opcion == 2:
                datos = obtener_indicador_diario("dolar")
                mostrar_indicador_diario(datos)

            elif opcion == 3:
                datos = obtener_indicador_diario("euro")
                mostrar_indicador_diario(datos)

            elif opcion == 4:
                datos = obtener_indicador_diario("uf")
                mostrar_indicador_diario(datos)

            elif opcion == 5:
                datos = obtener_indicador_diario("bitcoin")
                mostrar_indicador_diario(datos)

            elif opcion == 0:
                break
