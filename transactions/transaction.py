from abc import ABC, abstractmethod


class Transaction(ABC):

    @property
    @abstractmethod
    def amount(self):
        pass

    @abstractmethod
    def register(self, account):
        pass