from typing import Any, Iterable


def validar_tipo(valor: object, tipo: type) -> bool:
    try:
        tipo(valor)
    except ValueError:
        print("Tipo inválido")
        return False
    else:
        return True


def validar_opcion(opcion: Any, opciones: Iterable[Any]) -> bool:
    return True if opcion in opciones else False
