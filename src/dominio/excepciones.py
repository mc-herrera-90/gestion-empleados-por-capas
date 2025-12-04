class UsuarioNoEncontradoError(Exception):
    """Se lanza cuando un usuario no existe en la base de datos."""

    def __init__(self, mensaje: str = "Usuario no encontrado."):
        super().__init__(mensaje)


class CredencialesInvalidasError(Exception):
    """Se lanza cuando las credenciales (usuario/contraseña) son incorrectas."""

    def __init__(self, mensaje: str = "Usuario o contraseña incorrectos."):
        super().__init__(mensaje)


class EntradaInvalidaError(Exception):
    """Se lanza cuando un valor ingresado no cumple una regla de negocio."""

    def __init__(self, mensaje: str = "Entrada inválida."):
        super().__init__(mensaje)


class EmpleadoNoValidoError(Exception):
    """Se lanza cuando un empleado no cumple los criterios del dominio."""

    def __init__(self, mensaje: str = "Empleado no válido."):
        super().__init__(mensaje)


class DepartamentoDuplicadoError(Exception):
    """Se lanza cuando se intenta crear un departamento con nombre duplicado."""

    def __init__(self, mensaje: str = "Departamento duplicado."):
        super().__init__(mensaje)
