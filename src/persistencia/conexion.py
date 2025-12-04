import pymysql
from pymysql.connections import Connection
from typing import Optional, Iterable, Any
from configuracion.entorno import DB_HOST, DB_NAME
from configuracion.auditoria import logger_bd


class Conexion:

    def __init__(self, host: str = DB_HOST, database: str = DB_NAME) -> None:
        self._host = host
        self._database = database
        self._conn: Optional[Connection] = None

    def _conectar(self, user: str, password: str) -> Optional[Connection]:
        """
        Crea UNA conexión y la guarda en self._conn
        """
        try:
            self._conn = pymysql.connect(
                host=self._host, user=user, password=password, database=self._database
            )
            logger_bd.info(
                f"🔌 Conexión a MySQL exitosa: {user}@{self._host} -> {self._database}"
            )
            return self._conn

        except pymysql.MySQLError as e:
            logger_bd.error(f"😩 Error al conectar: {e}")
            self._conn = None
            return None

    def _desconectar(self) -> bool:
        """
        Cierra la conexión guardada en self._conn
        """
        if self._conn:
            try:
                self._conn.close()
                logger_bd.info("🔒 Conexión cerrada correctamente")
                self._conn = None
                return True
            except pymysql.MySQLError as e:
                print(f"[Conexion] Error al cerrar conexión: {e}")
                return False
        return False

    def _ejecutar_query(self, query: str, params: Optional[Iterable[Any]] = None):
        """
        Ejecuta SQL usando la conexión interna self._conn
        """
        if not self._conn:
            raise RuntimeError(
                "No hay conexión activa. Debes llamar _conectar() primero."
            )

        try:
            with self._conn.cursor() as cur:
                cur.execute(query, params)
                self._conn.commit()

                if query.strip().lower().startswith("select"):
                    return cur.fetchall()

                return cur.rowcount

        except pymysql.MySQLError as e:
            logger_bd.error(f"[Conexion] Error en ejecutar_query: {e}")
            return None
