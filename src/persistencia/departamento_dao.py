from dominio.departamento import Departamento
from persistencia.conexion import Conexion
from typing import List, Optional


class DepartamentoDAO:

    def __init__(self, conexion: Conexion, user: str, password: str):
        self._conexion = conexion
        self._user = user
        self._password = password
        self._conn = self._conexion.conectar(self._user, self._password)

    def _get_conn(self):
        """Reabre conexión si se perdió."""
        if self._conn is None or not self._conn.open:
            self._conn = self._conexion.conectar(self._user, self._password)
        return self._conn

    def agregar(self, depto: Departamento) -> bool:
        con = self._get_conn()

        query = """
            INSERT INTO departamento (nombre, descripcion)
            VALUES (%s, %s)
        """
        params = (depto.nombre, depto.descripcion)
        rowcount = self._conexion.ejecutar_query(con, query, params)
        return rowcount == 1

    def mostrar(self) -> List[Departamento]:
        con = self._get_conn()

        query = "SELECT id, nombre, descripcion FROM departamento"
        rows = self._conexion.ejecutar_query(con, query)

        return [Departamento(**row) for row in rows]

    def buscarPorCodigo(self, codigo: int) -> Optional[Departamento]:
        con = self._get_conn()

        query = "SELECT id, nombre, descripcion FROM departamento WHERE id = %s"
        rows = self._conexion.ejecutar_query(con, query, (codigo,))
        return Departamento(**rows[0]) if rows else None

    def buscarPorNombre(self, nombre: str) -> List[Departamento]:
        con = self._get_conn()

        query = "SELECT id, nombre, descripcion FROM departamento WHERE nombre LIKE %s"
        rows = self._conexion.ejecutar_query(con, query, (f"%{nombre}%",))
        return [Departamento(**row) for row in rows]

    def modificar(self, depto: Departamento) -> bool:
        con = self._get_conn()

        query = """
            UPDATE departamento
            SET nombre = %s, descripcion = %s, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """
        rowcount = self._conexion.ejecutar_query(
            con, query, (depto.nombre, depto.descripcion, depto.id)
        )
        return rowcount == 1

    def eliminar(self, depto: Departamento) -> bool:
        con = self._get_conn()

        query = "DELETE FROM departamento WHERE id = %s"
        rowcount = self._conexion.ejecutar_query(con, query, (depto.id,))
        return rowcount == 1
