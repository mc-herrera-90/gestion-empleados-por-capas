from typing import Optional
from datetime import date


class Proyecto:
    """
    Modelo de dominio para un Proyecto.

    Atributos:
        id (int): Identificador único asignado por la BD.
        nombre (str): Nombre del proyecto.
        descripcion (str | None): Descripción del proyecto.
        departamento_id (int | None): Departamento responsable del proyecto.
        fecha_inicio (date | None): Fecha de inicio del proyecto.
        fecha_fin (date | None): Fecha de término del proyecto.
        estado (str): Estado del proyecto.
    """

    ESTADOS_VALIDOS = {"planificado", "activo", "finalizado", "cancelado"}

    def __init__(
        self,
        nombre: str,
        descripcion: Optional[str] = None,
        departamento_id: Optional[int] = None,
        fecha_inicio: Optional[date] = None,
        fecha_fin: Optional[date] = None,
        estado: str = "planificado",
        id: Optional[int] = None,
    ) -> None:
        self._id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.departamento_id = departamento_id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    # ------------------------------------------------------------------
    # PROPIEDADES
    # ------------------------------------------------------------------

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("El id del proyecto no puede ser negativo.")
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or len(value.strip()) == 0:
            raise ValueError("El nombre del proyecto es obligatorio.")
        self._nombre = value.strip()

    @property
    def descripcion(self) -> Optional[str]:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: Optional[str]) -> None:
        self._descripcion = value.strip() if isinstance(value, str) else None

    @property
    def departamento_id(self) -> Optional[int]:
        return self._departamento_id

    @departamento_id.setter
    def departamento_id(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("El id del departamento debe ser positivo.")
        self._departamento_id = value

    @property
    def fecha_inicio(self) -> Optional[date]:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value: Optional[date]) -> None:
        self._fecha_inicio = value

    @property
    def fecha_fin(self) -> Optional[date]:
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, value: Optional[date]) -> None:
        if (
            value is not None
            and self.fecha_inicio is not None
            and value < self.fecha_inicio
        ):
            raise ValueError(
                "La fecha de fin no puede ser anterior a la fecha de inicio."
            )
        self._fecha_fin = value

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, value: str) -> None:
        if value not in self.ESTADOS_VALIDOS:
            raise ValueError(
                f"Estado inválido. Valores permitidos: {', '.join(self.ESTADOS_VALIDOS)}"
            )
        self._estado = value

    # ------------------------------------------------------------------
    # MÉTODOS DE NEGOCIO
    # ------------------------------------------------------------------

    def iniciar(self) -> None:
        if self.estado != "planificado":
            raise ValueError("Solo se puede iniciar un proyecto planificado.")
        self.estado = "activo"

    def finalizar(self) -> None:
        if self.estado != "activo":
            raise ValueError("Solo se puede finalizar un proyecto activo.")
        self.estado = "finalizado"

    def cancelar(self) -> None:
        if self.estado == "finalizado":
            raise ValueError("No se puede cancelar un proyecto finalizado.")
        self.estado = "cancelado"

    # ------------------------------------------------------------------
    # REPRESENTACIÓN
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Proyecto(id={self.id}, nombre='{self.nombre}', "
            f"estado='{self.estado}')"
        )
