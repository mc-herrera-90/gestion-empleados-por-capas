from dominio.proyecto import Proyecto
from persistencia.conexion import Conexion
from typing import List


class ProyectoDAO:

    def __init__(self, conexion: Conexion):
        """
        Recibe una instancia de Conexion ya configurada.
        No abre conexiones aquí (SRP).
        """
        self._conexion = conexion

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------
    def agregar(self, proyecto: Proyecto) -> bool:
        query = """
            INSERT INTO proyecto (
                nombre,
                descripcion,
                departamento_id,
                fecha_inicio,
                fecha_fin,
                estado
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            proyecto.nombre,
            proyecto.descripcion,
            proyecto.departamento_id,
            proyecto.fecha_inicio,
            proyecto.fecha_fin,
            proyecto.estado,
        )
        rowcount = self._conexion.ejecutar_query(query, params)
        return rowcount == 1

    # ------------------------------------------------------------------
    # READ ALL
    # ------------------------------------------------------------------
    def mostrar(self) -> List[Proyecto]:
        query = """
            SELECT
                id,
                nombre,
                descripcion,
                departamento_id,
                fecha_inicio,
                fecha_fin,
                estado
            FROM proyecto
        """
        rows = self._conexion.ejecutar_query(query)

        return [
            Proyecto(
                id=row["id"],
                nombre=row["nombre"],
                descripcion=row["descripcion"],
                departamento_id=row["departamento_id"],
                fecha_inicio=row["fecha_inicio"],
                fecha_fin=row["fecha_fin"],
                estado=row["estado"],
            )
            for row in rows
        ]

    # ------------------------------------------------------------------
    # READ ONE (ID)
    # ------------------------------------------------------------------
    def buscar_por_id(self, id_proyecto: int) -> Proyecto | None:
        query = "SELECT * FROM proyecto WHERE id = %s"
        rows = self._conexion.ejecutar_query(query, (id_proyecto,))

        if not rows:
            return None

        row = rows[0]
        return Proyecto(
            id=row["id"],
            nombre=row["nombre"],
            descripcion=row["descripcion"],
            departamento_id=row["departamento_id"],
            fecha_inicio=row["fecha_inicio"],
            fecha_fin=row["fecha_fin"],
            estado=row["estado"],
        )

    # ------------------------------------------------------------------
    # READ BY NAME
    # ------------------------------------------------------------------
    def buscar_por_nombre(self, nombre: str) -> List[Proyecto]:
        query = "SELECT * FROM proyecto WHERE nombre LIKE %s"
        rows = self._conexion.ejecutar_query(query, (f"%{nombre}%",))

        return [
            Proyecto(
                id=row["id"],
                nombre=row["nombre"],
                descripcion=row["descripcion"],
                departamento_id=row["departamento_id"],
                fecha_inicio=row["fecha_inicio"],
                fecha_fin=row["fecha_fin"],
                estado=row["estado"],
            )
            for row in rows
        ]

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------
    def modificar(self, proyecto: Proyecto) -> bool:
        query = """
            UPDATE proyecto
            SET
                nombre = %s,
                descripcion = %s,
                departamento_id = %s,
                fecha_inicio = %s,
                fecha_fin = %s,
                estado = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """
        params = (
            proyecto.nombre,
            proyecto.descripcion,
            proyecto.departamento_id,
            proyecto.fecha_inicio,
            proyecto.fecha_fin,
            proyecto.estado,
            proyecto.id,
        )
        rowcount = self._conexion.ejecutar_query(query, params)
        return rowcount == 1

    # ------------------------------------------------------------------
    # DELETE
    # ------------------------------------------------------------------
    def eliminar(self, id_proyecto: int) -> bool:
        query = "DELETE FROM proyecto WHERE id = %s"
        rowcount = self._conexion.ejecutar_query(query, (id_proyecto,))
        return rowcount == 1
