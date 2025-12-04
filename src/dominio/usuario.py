from typing import Optional


class Usuario:
    """
    Modelo de dominio para un Usuario del sistema.
    """

    def __init__(
        self,
        username: str,
        password_hash: str,
        id: Optional[int] = None,
    ) -> None:
        self._id = id
        self.username = username
        self.password_hash = password_hash

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: Optional[int]) -> None:
        if value is not None and value < 0:
            raise ValueError("El ID no puede ser negativo.")
        self._id = value

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        if not value or len(value.strip()) == 0:
            raise ValueError("El username es obligatorio.")
        if len(value) < 3:
            raise ValueError("El username debe tener al menos 3 caracteres.")
        self._username = value.strip()

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value: str) -> None:
        if not value or len(value.strip()) == 0:
            raise ValueError("El hash de contraseña no puede estar vacío.")
        self._password_hash = value.strip()

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, username='{self.username}')"
