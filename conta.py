
# Atribuição da classe conta como Abstract class 
# foram acrescentados atributos adicionais para a classe Conta:

from abc import ABC, abstractmethod
import historico
import clientes

class Conta:
    
    def __init__(
        self,
        #numero_conta: str,
        numero_agencia: str,
        saldo: float = 0.0,
    ) -> None:
        
        self._cliente = None
        self._numero_conta = None
        self._numero_agencia = numero_agencia
        self._historico_conta = {}
        self._saldo = saldo
        
    def __repr__(self) -> str:
        return  f'{self.__class__.__name__}:\n'\
                f'nome_titular_conta = {self._nome_titular_conta}\n'\
                f'cpf_titular_conta = {self._cpf_titular_conta}\n'\
                f'numero_conta = {self._numero_conta}\n'\
                f'numero_agencia = {self._numero_agencia}\n'\
                f'historico_conta = {self._historico_conta}\n'\
                f'saldo = {self._saldo:.2f})'




if __name__ == '__main__':
    
    c1 = Conta('Alex','453','010-9','0001-9')
    print(c1)
