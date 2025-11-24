from typing import Optional

class Empleado:
    """
    Modelo de dominio para un Empleado.

    Atributos:
        id (int): Identificador único asignado por la BD.
        nombre (str): Nombre del empleado.
        apellido (str): Apellido del empleado.
        departamento_id (int | None): ID del departamento al que pertenece.
    """

    def __init__(
        self,
        nombre: str,
        apellido: str,
        departamento_id: Optional[int] = None,
        id: Optional[int] = None,
    ) -> None:
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._departamento_id = departamento_id

    # PROPIEDADES

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        if value is not None and value < 0:
            raise ValueError("El id no puede ser negativo.")
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or len(value.strip()) == 0:
            raise ValueError("El nombre del empleado es obligatorio.")
        self._nombre = value.strip()

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, value: str) -> None:
        if not value or len(value.strip()) == 0:
            raise ValueError("El apellido es obligatorio.")
        self._apellido = value.strip()

    @property
    def departamento_id(self) -> Optional[int]:
        return self._departamento_id

    @departamento_id.setter
    def departamento_id(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("El id de departamento debe ser positivo.")
        self._departamento_id = value

    # MÉTODOS DE NEGOCIO

    def cambiar_departamento(self, nuevo_departamento_id: int) -> None:
        """
        Cambia el departamento del empleado.
        """
        if nuevo_departamento_id is None or nuevo_departamento_id < 0:
            raise ValueError("El ID de departamento no es válido.")
        self._departamento_id = nuevo_departamento_id

    # REPRESENTACIÓN
    def __repr__(self) -> str:
        return f"Empleado(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}')"
