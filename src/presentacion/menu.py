from abc import ABC, abstractmethod
from presentacion.utilidades import mostrar_mensaje_flush


class Menu(ABC):

    def __init__(self, titulo: str, opciones: list[str]) -> None:
        self.titulo = titulo
        self.opciones = opciones

    def mostrar_opciones(self):
        print(f"\n[ {self.titulo.upper()} ]\n")
        for i, op in enumerate(self.opciones, start=1):
            print(f"{i}. {op}")
        print("0. Volver al menú principal\n")

    def volverMenuPrincipal(self) -> None:

        mostrar_mensaje_flush("Volviendo al menú principal...\n")

    @abstractmethod
    def agregar(self) -> None:
        pass

    @abstractmethod
    def mostrarTodos(self) -> None:
        pass

    @abstractmethod
    def buscarPorCodigo(self) -> None:
        pass

    @abstractmethod
    def buscarPorNombre(self) -> None:
        pass

    @abstractmethod
    def modificar(self) -> None:
        pass

    @abstractmethod
    def eliminar(self):
        pass
