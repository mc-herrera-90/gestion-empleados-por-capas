from presentacion.validaciones import validar_tipo, validar_opcion
import time


def pedir_opcion_segura(mensaje: str, opciones_validas: list[int]) -> int:
    opcion_raw = input(mensaje)

    valido, opcion = validar_tipo(opcion_raw, int)
    while not valido:
        opcion_raw = input("Ingrese un número válido: ")
        valido, opcion = validar_tipo(opcion_raw, int)

    while not validar_opcion(opcion, opciones_validas):
        mostrar_mensaje_flush("Opción fuera de rango.\n")
        opcion_raw = input(mensaje)
        valido, opcion = validar_tipo(opcion_raw, int)

        while not valido:
            mostrar_mensaje_flush("Tipo inválido.\n")
            opcion_raw = input("Ingrese un número válido: ")
            valido, opcion = validar_tipo(opcion_raw, int)

    return opcion


def mostrar_mensaje_flush(
    mensaje: str = "Gracias por usar Ecotech Solutions ❤️",
    borde: bool = False,
) -> None:
    if borde:
        print("+" + "--" * (len(mensaje) // 2) + "--+")
        print(f"| ", end="")

    for letra in mensaje:
        print(f"{letra}", end="", flush=True)
        time.sleep(0.045)

    if borde:
        print(" |", end="")
        print()
        print("+" + "--" * (len(mensaje) // 2) + "--+")


def graficar_ascii(titulo: str, serie: list[dict]) -> None:
    max_valor = max(p["valor"] for p in serie)

    print(f"\n=== {titulo} últimos {len(serie)} días ===\n")

    for punto in serie:
        fecha = punto["fecha"].split("T")[0]
        valor = punto["valor"]
        largo = int((valor / max_valor) * 50)
        print(f"{fecha} | " + "#" * largo + f" {valor}%")
