from dominio.departamento import Departamento
from persistencia.conexion import Conexion
from typing import List


class DepartamentoDAO:

    def __init__(self, conexion: Conexion):
        """
        Recibe una instancia de Conexion ya configurada.
        No abre conexiones aquí (SRP).
        """
        self._conexion = conexion

    def agregar(self, depto: Departamento) -> bool:
        query = """
            INSERT INTO departamento (nombre, descripcion)
            VALUES (%s, %s)
        """
        params = (depto.nombre, depto.descripcion)
        rowcount = self._conexion.ejecutar_query(query, params)
        return rowcount == 1

    def mostrar(self) -> List[Departamento]:
        query = "SELECT id, nombre, descripcion FROM departamento"
        rows = self._conexion.ejecutar_query(query)

        return [
            Departamento(
                id=row["id"], nombre=row["nombre"], descripcion=row["descripcion"]
            )
            for row in rows
        ]

    def buscar_por_codigo(self, codigo: int) -> Departamento | None:
        query = "SELECT id, nombre, descripcion FROM departamento WHERE id = %s"
        rows = self._conexion.ejecutar_query(query, (codigo,))

        if not rows:
            return None

        row = rows[0]
        return Departamento(
            id=row["id"], nombre=row["nombre"], descripcion=row["descripcion"]
        )

    def buscar_por_nombre(self, nombre: str) -> List[Departamento]:
        query = "SELECT id, nombre, descripcion FROM departamento WHERE nombre LIKE %s"
        rows = self._conexion.ejecutar_query(query, (f"%{nombre}%",))

        return [
            Departamento(
                id=row["id"], nombre=row["nombre"], descripcion=row["descripcion"]
            )
            for row in rows
        ]

    def modificar(self, depto: Departamento) -> bool:
        query = """
            UPDATE departamento
            SET nombre = %s,
                descripcion = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """
        params = (depto.nombre, depto.descripcion, depto.id)
        rowcount = self._conexion.ejecutar_query(query, params)
        return rowcount == 1

    def eliminar(self, id_depto: int) -> bool:
        query = "DELETE FROM departamento WHERE id = %s"
        rowcount = self._conexion.ejecutar_query(query, (id_depto,))
        return rowcount == 1
