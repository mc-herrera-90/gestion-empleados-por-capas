import pymysql
from pymysql.connections import Connection
from configuracion.entorno import DB_HOST, DB_NAME, DB_USER, DB_USER_PASSWORD
from configuracion.auditoria import logger_bd
from persistencia.tipos import QueryResult, SQLParams


class Conexion:

    def __init__(
        self,
        host: str = DB_HOST,
        database: str = DB_NAME,
        user: str = DB_USER,
        password: str = DB_USER_PASSWORD,
    ) -> None:
        self._host = host
        self._database = database
        self._user = user
        self._password = password
        self._conn: Connection | None = None

    def _conectar(self) -> Connection | None:

        if self._conn and getattr(self._conn, "open", False):
            return self._conn

        try:
            self._conn = pymysql.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database,
            )
            logger_bd.info(
                f"🔌 Conexión a 🐬 MySQL exitosa: {self._user}@{self._host} -> {self._database}"
            )
            return self._conn

        except pymysql.MySQLError as e:
            logger_bd.error(f"😩 Error al conectar: {e}")
            self._conn = None
            return None

    def _desconectar(self) -> bool:
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

    def ejecutar_query(
        self, query: str, params: SQLParams = None
    ) -> QueryResult | int | None:
        if not self._conn:
            logger_bd.error(
                "❌ No se pudo establecer conexión con la BD antes de ejecutar query."
            )
            raise RuntimeError(
                "No hay conexión activa. Debes llamar _conectar() primero."
            )

        try:
            logger_bd.debug(f"[Conexion] Ejecutando query: {query} | params: {params}")

            with self._conn.cursor() as cur:
                cur.execute(query, params)
                self._conn.commit()

                if query.strip().lower().startswith("select"):
                    return cur.fetchall()

                return cur.rowcount

        except pymysql.MySQLError as e:
            logger_bd.error(f"[Conexion] Error en ejecutar_query: {e}")
            return None

    def abrir(self) -> bool:
        """Abre la conexión si no está abierta. Devuelve True si se conecta correctamente."""
        return self._conectar() is not None
