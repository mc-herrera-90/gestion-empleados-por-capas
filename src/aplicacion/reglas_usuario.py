import bcrypt
from dominio.usuario import Usuario
from dominio.excepciones import (
    UsuarioNoEncontradoError,
    CredencialesInvalidasError,
    EntradaInvalidaError,
)
from persistencia.usuario_dao import UsuarioDAO


class ReglasUsuario:
    """
    Capa de aplicación: maneja reglas de negocio de Usuario.
    Aquí se realiza hashing, login, creación, actualización y eliminación.
    """

    def __init__(self):
        self.dao = UsuarioDAO()

    def login(self, username: str, password: str) -> Usuario:
        try:
            usuario = self.dao.obtener_por_username(username)
        except UsuarioNoEncontradoError:
            raise CredencialesInvalidasError("Usuario o contraseña incorrectos.")

        # Comparar contraseña con bcrypt
        if not bcrypt.checkpw(
            password.encode("utf-8"), usuario.password_hash.encode("utf-8")
        ):
            raise CredencialesInvalidasError("Usuario o contraseña incorrectos.")

        return usuario

    def crear_usuario(self, username: str, password: str) -> Usuario:

        # Validación simple de entrada
        if len(username.strip()) < 3:
            raise EntradaInvalidaError(
                "El nombre de usuario debe tener al menos 3 caracteres."
            )

        if len(password) < 6:
            raise EntradaInvalidaError(
                "La contraseña debe tener al menos 6 caracteres."
            )

        # Hashear la contraseña
        password_hash = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode()

        # Crear objeto de dominio
        usuario = Usuario(username=username.strip(), password_hash=password_hash)

        # Guardar en DB
        self.dao.crear(usuario)

        return usuario

    # ----------------------------
    # MODIFICAR USUARIO
    # ----------------------------
    def modificar_usuario(
        self, user_id: int, nuevo_username: str, nueva_password: str
    ) -> None:

        if len(nuevo_username.strip()) < 3:
            raise EntradaInvalidaError(
                "El nombre de usuario debe tener al menos 3 caracteres."
            )

        if len(nueva_password) < 6:
            raise EntradaInvalidaError(
                "La contraseña debe tener al menos 6 caracteres."
            )

        # Hash de la nueva contraseña
        password_hash = bcrypt.hashpw(
            nueva_password.encode("utf-8"), bcrypt.gensalt()
        ).decode()

        usuario = Usuario(
            id=user_id, username=nuevo_username.strip(), password_hash=password_hash
        )

        self.dao.actualizar(usuario)

    # ----------------------------
    # CAMBIAR SOLO CONTRASEÑA
    # ----------------------------
    def cambiar_password(self, username: str, nueva_password: str) -> None:
        usuario = self.dao.obtener_por_username(username)

        if len(nueva_password) < 6:
            raise EntradaInvalidaError(
                "La contraseña debe tener al menos 6 caracteres."
            )

        password_hash = bcrypt.hashpw(
            nueva_password.encode("utf-8"), bcrypt.gensalt()
        ).decode()

        usuario.password_hash = password_hash
        self.dao.actualizar(usuario)

    # ----------------------------
    # ELIMINAR USUARIO
    # ----------------------------
    def eliminar_usuario(self, user_id: int) -> None:
        self.dao.eliminar(user_id)

    # ----------------------------
    # LISTAR TODOS
    # ----------------------------
    def listar_usuarios(self):
        return self.dao.listar()

    # ----------------------------
    # OBTENER POR USERNAME
    # ----------------------------
    def obtener_por_username(self, username: str) -> Usuario:
        return self.dao.obtener_por_username(username)

    # ----------------------------
    # OBTENER POR ID
    # ----------------------------
    def obtener_por_id(self, user_id: int) -> Usuario:
        return self.dao.obtener_por_id(user_id)
