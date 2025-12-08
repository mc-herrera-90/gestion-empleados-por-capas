"""
Tipos auxiliares para la capa de persistencia.

Estos tipos se utilizan para describir los resultados devueltos por queries SQL
y los parámetros que pueden recibir dichas consultas.
"""

from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

# Una fila devuelta por PyMySQL puede llegar como un dict:
# {"id": 1, "nombre": "Finanzas", "descripcion": "Depto contable"}
RowDict = Dict[str, Any]

# O como una tupla sin nombres:
# (1, "Finanzas", "Depto contable")
RowTuple = Tuple[Any, ...]

# Un resultado SELECT devuelve una lista de filas:
QueryResult = List[RowDict]

# Parámetros típicos para un query SQL:
# - Ninguno
# - Una tupla con valores
# - Una lista con valores
SQLParams = Optional[Union[Tuple[Any, ...], List[Any], Iterable[Any]]]
