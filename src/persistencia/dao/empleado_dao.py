from dominio.empleado import Empleado
from persistencia.conexion import Conexion
from typing import List


class EmpleadoDAO:

    def __init__(self, conexion: Conexion):
        """
        Recibe una instancia de Conexion ya configurada.
        No abre conexiones aquí (SRP).
        """
        self._conexion = conexion

    def agregar(self, empleado: Empleado) -> bool:
        query = """
            INSERT INTO empleado (
                rut,
                nombre,
                apellido,
                direccion,
                telefono,
                correo,
                fecha_contrato,
                salario,
                departamento_id,
                proyecto_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            empleado.rut,
            empleado.nombre,
            empleado.apellido,
            empleado.direccion,
            empleado.telefono,
            empleado.correo,
            empleado.fecha_contrato,
            empleado.salario,
            empleado.departamento_id,
            empleado.proyecto_id,
        )
        rowcount = self._conexion.ejecutar_query(query, params)
        return rowcount == 1

    def mostrar(self) -> List[Empleado]:
        query = """
            SELECT
                id,
                rut,
                nombre,
                apellido,
                direccion,
                telefono,
                correo,
                fecha_contrato,
                salario,
                departamento_id,
                proyecto_id
            FROM empleado
        """
        rows = self._conexion.ejecutar_query(query)

        return [
            Empleado(
                id=row["id"],
                rut=row["rut"],
                nombre=row["nombre"],
                apellido=row["apellido"],
                direccion=row["direccion"],
                telefono=row["telefono"],
                correo=row["correo"],
                fecha_contrato=row["fecha_contrato"],
                salario=row["salario"],
                departamento_id=row["departamento_id"],
                proyecto_id=row["proyecto_id"],
            )
            for row in rows
        ]

    def buscar_por_id(self, id_empleado: int) -> Empleado | None:
        query = "SELECT * FROM empleado WHERE id = %s"
        rows = self._conexion.ejecutar_query(query, (id_empleado,))

        if not rows:
            return None

        row = rows[0]
        return Empleado(
            id=row["id"],
            rut=row["rut"],
            nombre=row["nombre"],
            apellido=row["apellido"],
            direccion=row["direccion"],
            telefono=row["telefono"],
            correo=row["correo"],
            fecha_contrato=row["fecha_contrato"],
            salario=row["salario"],
            departamento_id=row["departamento_id"],
            proyecto_id=row["proyecto_id"],
        )

    def buscar_por_rut(self, rut: str) -> Empleado | None:
        query = "SELECT * FROM empleado WHERE rut = %s"
        rows = self._conexion.ejecutar_query(query, (rut,))

        if not rows:
            return None

        row = rows[0]
        return Empleado(
            id=row["id"],
            rut=row["rut"],
            nombre=row["nombre"],
            apellido=row["apellido"],
            direccion=row["direccion"],
            telefono=row["telefono"],
            correo=row["correo"],
            fecha_contrato=row["fecha_contrato"],
            salario=row["salario"],
            departamento_id=row["departamento_id"],
            proyecto_id=row["proyecto_id"],
        )

    def buscar_por_nombre(self, nombre: str) -> List[Empleado]:
        query = """
            SELECT * FROM empleado
            WHERE nombre LIKE %s OR apellido LIKE %s
        """
        rows = self._conexion.ejecutar_query(query, (f"%{nombre}%", f"%{nombre}%"))

        return [
            Empleado(
                id=row["id"],
                rut=row["rut"],
                nombre=row["nombre"],
                apellido=row["apellido"],
                direccion=row["direccion"],
                telefono=row["telefono"],
                correo=row["correo"],
                fecha_contrato=row["fecha_contrato"],
                salario=row["salario"],
                departamento_id=row["departamento_id"],
                proyecto_id=row["proyecto_id"],
            )
            for row in rows
        ]

    def modificar(self, empleado: Empleado) -> bool:
        query = """
            UPDATE empleado
            SET
                rut = %s,
                nombre = %s,
                apellido = %s,
                direccion = %s,
                telefono = %s,
                correo = %s,
                fecha_contrato = %s,
                salario = %s,
                departamento_id = %s,
                proyecto_id = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """
        params = (
            empleado.rut,
            empleado.nombre,
            empleado.apellido,
            empleado.direccion,
            empleado.telefono,
            empleado.correo,
            empleado.fecha_contrato,
            empleado.salario,
            empleado.departamento_id,
            empleado.proyecto_id,
            empleado.id,
        )
        rowcount = self._conexion.ejecutar_query(query, params)
        return rowcount == 1

    def eliminar(self, id_empleado: int) -> bool:
        query = "DELETE FROM empleado WHERE id = %s"
        rowcount = self._conexion.ejecutar_query(query, (id_empleado,))
        return rowcount == 1
