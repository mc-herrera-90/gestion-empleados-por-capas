import pymysql
from pymysql.connections import Connection
from typing import Optional, Iterable, Any
from configuracion.entorno import DB_HOST, DB_NAME
from configuracion.auditoria import logger_bd


class Conexion:
    """
    Clase base para gestionar la conexión a MySQL y gestionar un Cursor para ejecutar sentencias SQL.
    """

    def __init__(
        self,
        host: str = DB_HOST,
        database: str = DB_NAME,
    ) -> None:
        self._host = host
        self._database = database

    def conectar(self, user: str, password: str) -> Optional[Connection]:
        """
        Intenta una conexión ÚNICA.
        La capa aplicación decide si reintenta o no.
        """
        conn = None
        try:
            conn = pymysql.connect(
                host=self._host, user=user, password=password, database=self._database
            )
            logger_bd.info(
                f"🔌 Conexión a 🐬 MySQL exitosa :🧑🏻‍💻 {user}@{self._host} -> 💾 {self._database}"
            )
            return conn

        except pymysql.MySQLError as e:
            logger_bd.error(f"😩 Error al conectar: {e}")
            self.desconectar(conn)
            return None

    def desconectar(self, conexion: Connection) -> bool:
        """
        Cierra la conexión abierta.
        """
        if conexion:
            try:
                conexion.close()
                logger_bd.info(f"🔒 Conexión cerrada correctamente")
                return True
            except pymysql.MySQLError as e:
                print(f"[Conexion] Error al cerrar conexión: {e}")
                return False
        return False

    def ejecutar_query(
        self,
        conexion: Connection,
        query: str,
        params: Optional[Iterable[Any]] = None,
    ):
        """
        Ejecuta un query (SELECT, INSERT, UPDATE o DELETE).
        Retorna:
            - lista de rows para SELECT
            - cantidad de filas afectadas en otros casos
        """
        try:
            with conexion.cursor() as cur:
                cur.execute(query, params)
                conexion.commit()

                if query.strip().lower().startswith("select"):
                    return cur.fetchall()

                return cur.rowcount

        except pymysql.MySQLError as e:
            print(f"[Conexion] Error en ejecutar_query: {e}")
            return None
