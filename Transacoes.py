from abc import ABC, abstractmethod
from datetime import datetime as dt


class Transacoes(ABC):
    
    def debito(self):...