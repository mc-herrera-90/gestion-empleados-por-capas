from typing import Optional
from datetime import date


class Empleado:
    """
    Modelo de dominio para un Empleado.
    """

    def __init__(
        self,
        rut: str,
        nombre: str,
        apellido: str,
        correo: str,
        direccion: Optional[str] = None,
        telefono: Optional[str] = None,
        fecha_contrato: Optional[date] = None,
        salario: Optional[int] = None,
        departamento_id: Optional[int] = None,
        proyecto_id: Optional[int] = None,
        id: Optional[int] = None,
    ) -> None:
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_contrato = fecha_contrato
        self.salario = salario
        self.departamento_id = departamento_id
        self.proyecto_id = proyecto_id

    # ─────────────────────
    # PROPIEDADES
    # ─────────────────────

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("El id no puede ser negativo.")
        self._id = value

    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El RUT es obligatorio.")
        self._rut = value.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El nombre es obligatorio.")
        self._nombre = value.strip()

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El apellido es obligatorio.")
        self._apellido = value.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, value: str) -> None:
        if not value or "@" not in value:
            raise ValueError("Correo inválido.")
        self._correo = value.strip()

    @property
    def direccion(self) -> Optional[str]:
        return self._direccion

    @direccion.setter
    def direccion(self, value: Optional[str]) -> None:
        if value is None:
            self._direccion = None
        else:
            self._direccion = value.strip()

    @property
    def telefono(self) -> Optional[str]:
        return self._telefono

    @telefono.setter
    def telefono(self, value: Optional[str]) -> None:
        if value is None:
            self._telefono = None
        else:
            self._telefono = value.strip()

    @property
    def fecha_contrato(self) -> Optional[date]:
        return self._fecha_contrato

    @fecha_contrato.setter
    def fecha_contrato(self, value: Optional[date]) -> None:
        self._fecha_contrato = value

    @property
    def salario(self) -> Optional[int]:
        return self._salario

    @salario.setter
    def salario(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario = value

    @property
    def departamento_id(self) -> Optional[int]:
        return self._departamento_id

    @departamento_id.setter
    def departamento_id(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("Departamento inválido.")
        self._departamento_id = value

    @property
    def proyecto_id(self) -> Optional[int]:
        return self._proyecto_id

    @proyecto_id.setter
    def proyecto_id(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("Proyecto inválido.")
        self._proyecto_id = value

    # ─────────────────────
    # REPRESENTACIÓN
    # ─────────────────────

    def __repr__(self) -> str:
        return (
            f"Empleado(id={self.id}, rut='{self.rut}', "
            f"nombre='{self.nombre}', apellido='{self.apellido}')"
        )
