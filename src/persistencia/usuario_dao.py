from typing import List
from dominio.usuario import Usuario
from dominio.excepciones import UsuarioNoEncontradoError
from persistencia.conexion import Conexion
from configuracion.entorno import DB_USER, DB_USER_PASSWORD


class UsuarioDAO:
    """
    Clase responsable de manejar la persistencia de usuarios en la BD.
    CRUD: crear, obtener, actualizar, eliminar, listar.
    """

    def __init__(self) -> None:
        self._conexion = Conexion()
        self._conn = self._conexion.conectar(DB_USER, DB_USER_PASSWORD)

    # CREAR
    def crear(self, usuario: Usuario) -> None:
        sql = "INSERT INTO usuarios (username, password_hash) VALUES (%s, %s)"
        rows = self._conexion.ejecutar_query(
            self._conn, sql, (usuario.username, usuario.password_hash)
        )

        if rows is None:
            raise Exception("Error al insertar usuario")

        usuario.id = self._conn.insert_id()

    # OBTENER POR USERNAME
    def obtener_por_username(self, username: str) -> Usuario:
        conn = self._conexion.conectar(DB_USER, DB_USER_PASSWORD)
        if not conn:
            raise ConnectionError("No se pudo conectar a la base de datos.")

        sql = "SELECT id, username, password_hash FROM usuarios WHERE username = %s"

        with conn.cursor() as cursor:
            cursor.execute(sql, (username,))
            fila = cursor.fetchone()

        self._conexion.desconectar(conn)

        if not fila:
            raise UsuarioNoEncontradoError("Usuario no encontrado.")

        return Usuario(id=fila[0], username=fila[1], password_hash=fila[2])

    # OBTENER POR ID
    def obtener_por_id(self, user_id: int) -> Usuario:
        conn = self._conexion.conectar(DB_USER, DB_USER_PASSWORD)
        if not conn:
            raise ConnectionError("No se pudo conectar a la base de datos.")

        sql = "SELECT id, username, password_hash FROM usuarios WHERE id = %s"

        with conn.cursor() as cursor:
            cursor.execute(sql, (user_id,))
            fila = cursor.fetchone()

        self._conexion.desconectar(conn)

        if not fila:
            raise UsuarioNoEncontradoError(f"Usuario con ID {user_id} no existe.")

        return Usuario(id=fila[0], username=fila[1], password_hash=fila[2])

    # ACTUALIZAR
    def actualizar(self, usuario: Usuario) -> None:
        conn = self._conexion.conectar(DB_USER, DB_USER_PASSWORD)
        if not conn:
            raise ConnectionError("No se pudo conectar a la base de datos.")

        sql = "UPDATE usuarios SET username = %s, password_hash = %s WHERE id = %s"

        with conn.cursor() as cursor:
            cursor.execute(sql, (usuario.username, usuario.password_hash, usuario.id))
            conn.commit()

        self._conexion.desconectar(conn)

    # ELIMINAR
    def eliminar(self, user_id: int) -> None:
        conn = self._conexion.conectar(DB_USER, DB_USER_PASSWORD)
        if not conn:
            raise ConnectionError("No se pudo conectar a la base de datos.")

        sql = "DELETE FROM usuarios WHERE id = %s"

        with conn.cursor() as cursor:
            cursor.execute(sql, (user_id,))
            conn.commit()

        self._conexion.desconectar(conn)

    # LISTAR TODOS
    def listar(self) -> List[Usuario]:
        conn = self._conexion.conectar(DB_USER, DB_USER_PASSWORD)
        if not conn:
            raise ConnectionError("No se pudo conectar a la base de datos.")

        sql = "SELECT id, username, password_hash FROM usuarios"

        with conn.cursor() as cursor:
            cursor.execute(sql)
            filas = cursor.fetchall()

        self._conexion.desconectar(conn)

        return [Usuario(id=f[0], username=f[1], password_hash=f[2]) for f in filas]
