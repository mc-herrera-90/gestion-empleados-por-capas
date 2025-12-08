"""
Script de inicialización de la base de datos.
No pertenece a ninguna capa de arquitectura: solo prepara el esquema inicial.
"""

import os
import pymysql
from configuracion.entorno import ROOT_PATH, DB_HOST
from configuracion.auditoria import logger_bd
from pwinput import pwinput


class GestorInicializacion:
    """
    Clase que ejecuta el archivo SQL que define la estructura inicial
    de la base de datos. Debe ejecutarse con credenciales de root.
    """

    MAX_INTENTOS = 3

    def __init__(self, archivo_esquema: str):
        self.archivo_esquema = os.path.join(ROOT_PATH, "sql", archivo_esquema)

    def _conectar_root(self, usuario: str, password: str):
        try:
            return pymysql.connect(
                host=DB_HOST, user=usuario, password=password, autocommit=False
            )
        except pymysql.MySQLError as e:
            logger_bd.error(f"[init_db] Fallo al conectar como root: {e}")

            return None

    def _pedir_credenciales_root(self):
        """Solicita credenciales al usuario hasta que se conecte o se agoten los intentos."""
        for intento in range(1, self.MAX_INTENTOS + 1):
            print(f"\nIntento {intento}/{self.MAX_INTENTOS}")
            usuario = input("Usuario root MySQL: ").strip()
            password = pwinput("Contraseña root MySQL: ")

            con = self._conectar_root(usuario, password)
            if con:
                logger_bd.info(f"[init_db] Conexión root exitosa en intento {intento}")
                print("✅ Conexión como root exitosa.\n")
                return con

            print("[ERROR] Credenciales inválidas. Intenta nuevamente.")

        print("\n✖ No se pudo conectar después de varios intentos.")
        return None

    def _listar_tablas(self, con, db_name: str):
        """Muestra las tablas creadas en la base de datos."""
        try:
            with con.cursor() as cur:
                cur.execute(f"SHOW TABLES FROM {db_name}")
                tablas = [row[0] for row in cur.fetchall()]
                if tablas:
                    print("📋 Tablas creadas en la base de datos:")
                    for t in tablas:
                        print(f" - {t}")
                else:
                    print("⚠ No se encontraron tablas en la base de datos.")
        except pymysql.MySQLError as e:
            print(f"[ERROR] No se pudo listar las tablas: {e}")

    def _mostrar_usuario_administrador(
        self,
        con,
        usuario: str,
        host: str = DB_HOST,
        db_name: str = "ecotech_solutions_company",
        password: str = "Admin123!",
    ):
        """Muestra información del usuario administrador, sus permisos y credenciales de conexión."""
        try:
            with con.cursor() as cur:
                # Info usuario y plugin
                cur.execute(
                    "SELECT user, host, plugin FROM mysql.user WHERE user = %s AND host = %s",
                    (usuario, host),
                )
                user_info = cur.fetchone()
                if user_info:
                    print(
                        f"\n✅ Usuario administrador configurado: {user_info[0]}@{user_info[1]}"
                    )
                    print(f"Plugin de autenticación: {user_info[2]}\n")
                else:
                    print(f"\n⚠ No se encontró el usuario '{usuario}'@'{host}'")
                    return

                # Permisos
                cur.execute(f"SHOW GRANTS FOR '{usuario}'@'{host}'")
                grants = [row[0] for row in cur.fetchall()]

                global_grants = [g for g in grants if "*.*" in g.upper()]
                db_grants = [g for g in grants if f"`{db_name}`.*" in g]

                print("Permisos asignados:")
                if global_grants:
                    print(" - Global:")
                    for g in global_grants:
                        print(f"     {g}")
                if db_grants:
                    print(" - Proyecto:")
                    for g in db_grants:
                        print(f"     {g}")

                # Credenciales app
                print("\n🔑 Credenciales para conectar desde la aplicación:")
                print(f"Usuario: {usuario}")
                print(f"Contraseña: {password}")

        except pymysql.MySQLError as e:
            print(f"[ERROR] No se pudo obtener info del usuario administrador: {e}")

    def inicializar(self):
        """Ejecuta el archivo SQL para crear base de datos, tablas y usuarios."""
        print("\n=== Inicialización de Base de Datos ===\n")

        # Cargar archivo SQL
        try:
            with open(self.archivo_esquema, "r", encoding="utf-8") as f:
                sql_script = f.read()
        except FileNotFoundError:
            print(f"[ERROR] No existe el archivo SQL: {self.archivo_esquema}")
            return False
        except IOError as e:
            print(f"[ERROR] No se pudo leer el archivo SQL: {e}")
            return False

        print(f"Archivo SQL: {self.archivo_esquema}\n✅  cargado correctamente.\n")

        con = self._pedir_credenciales_root()
        if con is None:
            return False

        try:
            sentencias = [s.strip() for s in sql_script.split(";") if s.strip()]

            with con.cursor() as cur:
                for sentencia in sentencias:
                    cur.execute(sentencia)

            con.commit()

            # Mostrar base de datos inicializada
            print("✅ Base de datos inicializada correctamente.\n")
            self._listar_tablas(con, "ecotech_solutions_company")

            # Mostrar usuario admin, permisos y credenciales
            self._mostrar_usuario_administrador(con, "ecotech_admin")

            return True

        except pymysql.MySQLError as e:
            print(f"[ERROR SQL] {e}")
            return False

        finally:
            con.close()


def inicializar_db(archivo_esquema="schema.sql"):
    """Entry-point CLI."""
    gestor = GestorInicializacion(archivo_esquema)
    return gestor.inicializar()


if __name__ == "__main__":
    inicializar_db()
