from typing import List
from dominio.usuario import Usuario
from dominio.excepciones import UsuarioNoEncontradoError
from persistencia.conexion import Conexion


class UsuarioDAO:
    """
    Persistencia de usuarios (CRUD).
    """

    def __init__(self, conexion: Conexion) -> None:
        self._conexion = conexion

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------
    def crear(self, usuario: Usuario) -> None:
        sql_insert = """
            INSERT INTO usuarios (username, password_hash)
            VALUES (%s, %s)
        """

        rowcount = self._conexion.ejecutar_query(
            sql_insert,
            (usuario.username, usuario.password_hash),
        )

        if rowcount != 1:
            raise Exception("Error al insertar usuario")

        # ✅ obtener el ID generado POR MYSQL
        sql_id = "SELECT LAST_INSERT_ID() AS id"
        rows = self._conexion.ejecutar_query(sql_id)

        usuario.id = rows[0]["id"]

    # ------------------------------------------------------------------
    # READ BY USERNAME
    # ------------------------------------------------------------------
    def obtener_por_username(self, username: str) -> Usuario:
        sql = """
            SELECT id, username, password_hash
            FROM usuarios
            WHERE username = %s
        """
        rows = self._conexion.ejecutar_query(sql, (username,))

        if not rows:
            raise UsuarioNoEncontradoError("Usuario no encontrado.")

        return Usuario(**rows[0])

    # ------------------------------------------------------------------
    # READ BY ID
    # ------------------------------------------------------------------
    def obtener_por_id(self, user_id: int) -> Usuario:
        sql = """
            SELECT id, username, password_hash
            FROM usuarios
            WHERE id = %s
        """
        rows = self._conexion.ejecutar_query(sql, (user_id,))

        if not rows:
            raise UsuarioNoEncontradoError(f"Usuario con ID {user_id} no existe.")

        return Usuario(**rows[0])

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------
    def actualizar(self, usuario: Usuario) -> None:
        sql = """
            UPDATE usuarios
            SET username = %s,
                password_hash = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """
        rowcount = self._conexion.ejecutar_query(
            sql,
            (usuario.username, usuario.password_hash, usuario.id),
        )

        if rowcount != 1:
            raise UsuarioNoEncontradoError(
                f"No se pudo actualizar el usuario con ID {usuario.id}"
            )

    # ------------------------------------------------------------------
    # DELETE
    # ------------------------------------------------------------------
    def eliminar(self, user_id: int) -> None:
        sql = "DELETE FROM usuarios WHERE id = %s"
        rowcount = self._conexion.ejecutar_query(sql, (user_id,))

        if rowcount != 1:
            raise UsuarioNoEncontradoError(
                f"No se pudo eliminar el usuario con ID {user_id}"
            )

    # ------------------------------------------------------------------
    # READ ALL
    # ------------------------------------------------------------------
    def listar(self) -> List[Usuario]:
        sql = "SELECT id, username, password_hash FROM usuarios"
        rows = self._conexion.ejecutar_query(sql)
        return [Usuario(**row) for row in rows]
