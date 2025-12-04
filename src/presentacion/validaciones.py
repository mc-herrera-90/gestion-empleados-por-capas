from typing import Any, Iterable


def validar_tipo(valor: str, tipo: type) -> tuple[bool, Any]:
    try:
        return True, tipo(valor)
    except ValueError:
        return False, None


def validar_opcion(opcion: Any, opciones: Iterable[Any]) -> bool:
    return opcion in opciones
