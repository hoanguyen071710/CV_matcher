from abc import ABC, abstractmethod

class Connection(ABC):
    @abstractmethod
    def getEngine(self): ...
