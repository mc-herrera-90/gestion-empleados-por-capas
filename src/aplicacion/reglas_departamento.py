from persistencia.departamento_dao import DepartamentoDAO
from dominio.departamento import Departamento
from typing import List, Optional

class ReglasDepartamento:
  def __init__(self, dao: DepartamentoDAO):
    self.dao = dao

  def crear_objeto(self, nombre: str, descripcion: str = None) -> bool:
    d = Departamento(nombre=nombre, descripcion=descripcion)
    return self.dao.agregar(d)

  def mostrar_todos(self) -> List[Departamento]:
    return self.dao.mostrar()

  def buscar(self, valor) -> Optional[Departamento]:
    return self.dao.buscar(valor)

  def modificar(self, depto: Departamento) -> bool:
    return self.dao.modificar(depto)

  def eliminar(self, depto: Departamento) -> bool:
    return self.dao.eliminar(depto)
