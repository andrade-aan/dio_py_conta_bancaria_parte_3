
# Atribuição da classe conta como Abstract class 
# foram acrescentados atributos adicionais para a classe Conta:

from abc import ABC, abstractmethod
import historico
import clientes, servicos


class Conta(ABC):
    
    bco_agencia_numero = '0001-9'
    
    contas_da_agencia =[]
    
    @abstractmethod
    def __init__(
        self, cliente_cpf, numero_conta,
        numero_agencia: str='0001-9',
        saldo: float = 0.0,
    ) -> None:
        
        self._cliente_cpf = cliente_cpf
        self._numero_conta = numero_conta
        self._numero_agencia = numero_agencia
        self._historico_conta = {}
        self._saldo = saldo
        
    def __repr__(self) -> str:
        return  f'{self.__class__.__name__}:\n'\
                f'cliente_cpf = {self._cliente_cpf}\n'\
                f'numero_conta = {self._numero_conta}\n'\
                f'numero_agencia = {self._numero_agencia}\n'\
                f'saldo = {self._saldo:.2f}'


class ContaCorrente(Conta):
    
    def __init__(self, cliente_cpf, numero_conta,
                 numero_agencia, saldo, limite):
        
        self._limite = limite
        super().__init__(cliente_cpf, numero_conta, 
                         numero_agencia, saldo)
    @classmethod
    def criar_nova_conta_corrente(cls, cliente_cpf, numero_conta,
                 numero_agencia, saldo, limite):...


if __name__ == '__main__':
    
    c1 = ContaCorrente('463','0012','0001',0)
    print(c1)
