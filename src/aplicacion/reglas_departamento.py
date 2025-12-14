from persistencia.departamento_dao import DepartamentoDAO
from dominio.departamento import Departamento
from typing import List, Optional


class ReglasDepartamento:

    def __init__(self, dao: DepartamentoDAO):
        """
        Regla de negocio para departamento.
        Recibe un DAO ya configurado con la conexión.
        """
        self.dao = dao

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------
    def crear_objeto(self, nombre: str, descripcion: str | None = None) -> bool:
        depto = Departamento(nombre=nombre, descripcion=descripcion)
        return self.dao.agregar(depto)

    # ------------------------------------------------------------------
    # READ ALL
    # ------------------------------------------------------------------
    def mostrar_todos(self) -> List[Departamento]:
        return self.dao.mostrar()

    # ------------------------------------------------------------------
    # READ ONE (elige si es ID o NOMBRE)
    # ------------------------------------------------------------------
    def buscar(self, valor: str | int) -> List[Departamento] | Optional[Departamento]:
        """
        Si valor es int → buscar por código.
        Si valor es str → buscar por nombre.
        """
        if isinstance(valor, int):
            return self.dao.buscar_por_codigo(valor)
        return self.dao.buscar_por_nombre(valor)

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------
    def modificar(self, depto: Departamento) -> bool:
        return self.dao.modificar(depto)

    # ------------------------------------------------------------------
    # DELETE
    # ------------------------------------------------------------------
    def eliminar(self, id_depto: int) -> bool:
        return self.dao.eliminar(id_depto)
