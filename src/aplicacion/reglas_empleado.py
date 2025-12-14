from persistencia.dao.empleado_dao import EmpleadoDAO
from persistencia.dao.departamento_dao import DepartamentoDAO
from persistencia.dao.proyecto_dao import ProyectoDAO
from dominio.empleado import Empleado
from typing import List, Optional


class ReglasEmpleado:

    def __init__(
        self,
        empleado_dao: EmpleadoDAO,
        departamento_dao: DepartamentoDAO,
        proyecto_dao: ProyectoDAO | None = None,
    ):
        """
        Regla de negocio para Empleado.
        Recibe los DAO ya configurados con la conexión.
        """
        self.empleado_dao = empleado_dao
        self.departamento_dao = departamento_dao
        self.proyecto_dao = proyecto_dao

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------
    def crear_objeto(
        self,
        rut: str,
        nombre: str,
        apellido: str,
        correo: str,
        direccion: str | None = None,
        telefono: str | None = None,
        fecha_contrato=None,
        salario: int | None = None,
        departamento_id: int | None = None,
        proyecto_id: int | None = None,
    ) -> bool:
        """
        Regla:
        - No se puede crear un empleado sin departamento.
        - El departamento debe existir.
        - Si se indica proyecto, debe existir.
        """

        # 🔴 Regla de negocio: departamento obligatorio
        if departamento_id is None:
            raise ValueError("El empleado debe pertenecer a un departamento.")

        # 🔴 Regla de negocio: departamento válido
        if not self.departamento_dao.buscar_por_codigo(departamento_id):
            raise ValueError("El departamento indicado no existe.")

        # 🔴 Regla de negocio opcional: proyecto válido
        if proyecto_id is not None and self.proyecto_dao:
            if not self.proyecto_dao.buscar_por_id(proyecto_id):
                raise ValueError("El proyecto indicado no existe.")

        empleado = Empleado(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            fecha_contrato=fecha_contrato,
            salario=salario,
            departamento_id=departamento_id,
            proyecto_id=proyecto_id,
        )

        return self.empleado_dao.agregar(empleado)

    # ------------------------------------------------------------------
    # READ ALL
    # ------------------------------------------------------------------
    def mostrar_todos(self) -> List[Empleado]:
        return self.empleado_dao.mostrar()

    # ------------------------------------------------------------------
    # READ ONE (ID / RUT / NOMBRE)
    # ------------------------------------------------------------------
    def buscar(self, valor: str | int) -> List[Empleado] | Optional[Empleado]:
        """
        Si valor es int → buscar por ID.
        Si valor es str y parece RUT → buscar por RUT.
        Si valor es str → buscar por nombre/apellido.
        """

        if isinstance(valor, int):
            return self.empleado_dao.buscar_por_id(valor)

        if isinstance(valor, str) and "-" in valor:
            return self.empleado_dao.buscar_por_rut(valor)

        return self.empleado_dao.buscar_por_nombre(valor)

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------
    def modificar(self, empleado: Empleado) -> bool:
        """
        Regla:
        - No permitir quitar el departamento.
        """

        if empleado.departamento_id is None:
            raise ValueError("El empleado debe pertenecer a un departamento.")

        if not self.departamento_dao.buscar_por_codigo(empleado.departamento_id):
            raise ValueError("El departamento indicado no existe.")

        return self.empleado_dao.modificar(empleado)

    # ------------------------------------------------------------------
    # DELETE
    # ------------------------------------------------------------------
    def eliminar(self, id_empleado: int) -> bool:
        return self.empleado_dao.eliminar(id_empleado)
