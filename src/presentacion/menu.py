from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def mostrar_opciones(self):
        pass

    @abstractmethod
    def seleccionar_opcion(self, opcion):
        pass