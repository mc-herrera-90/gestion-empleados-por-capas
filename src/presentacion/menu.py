from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def mostrar_opciones(self):
        pass
