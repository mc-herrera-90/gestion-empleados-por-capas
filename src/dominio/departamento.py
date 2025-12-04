from typing import Optional


class Departamento:
    """
    Modelo de dominio para un Departamento.

    Atributos:
        id (int | None): Identificador único asignado por la BD.
        nombre (str): Nombre del departamento.
        descripcion (str | None): Descripción opcional del departamento.
    """

    def __init__(
        self,
        nombre: str,
        descripcion: Optional[str] = None,
        id: Optional[int] = None,
    ) -> None:
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        if value is not None and value < 0:
            raise ValueError("El ID no puede ser negativo.")
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or len(value.strip()) == 0:
            raise ValueError("El nombre del departamento es obligatorio.")
        self._nombre = value.strip()

    @property
    def descripcion(self) -> Optional[str]:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: Optional[str]) -> None:
        if value is not None and len(value.strip()) == 0:
            value = None  # Normalizamos descripción vacía
        self._descripcion = value

    def __repr__(self) -> str:
        return f"Departamento(id={self.id}, nombre='{self.nombre}')"
