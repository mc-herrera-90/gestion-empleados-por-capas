from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def mostrar_opciones(self):
        pass

    @abstractmethod
    def mostrarTodos(self):
        pass
    @abstractmethod
    def buscarPorCodigo(self):
        pass
    @abstractmethod
    def buscarPorNombre(self):
        pass
    @abstractmethod
    def modificar(self):
        pass
    @abstractmethod
    def eliminar(self):
        pass
    @abstractmethod
    def volverMenuPrincipal(self):
        pass
