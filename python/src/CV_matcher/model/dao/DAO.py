from abc import ABC, abstractmethod


class DAO(ABC):

    @abstractmethod
    def insert(self, t: object):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def update(self, t: object):
        pass