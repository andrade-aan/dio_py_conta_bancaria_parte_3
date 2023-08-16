
# Atribuição da classe conta como Abstract class 
# foram acrescentados atributos adicionais para a classe Conta:

from abc import ABC, abstractmethod
import historico
import clientes, servicos


class Conta(ABC):
    
    bco_agencia_numero = '0001-9'
    
    relacao_contas_da_agencia =[]
    
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
   
   
    @property
    def cliente_cpf(self):
        return self._cliente_cpf
    
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    
    @property
    def numero_agencia(self):
        return self._numero_agencia
    
    
    @property
    def saldo(self):
        return self._saldo
    

class ContaCorrente(Conta):
    
    def __init__(self, cliente_cpf, numero_conta,
                 numero_agencia, saldo, limite):
        
        self._limite = limite
        super().__init__(cliente_cpf, numero_conta, 
                         numero_agencia, saldo)
   
   
    @classmethod
    def db_adicionar_conta(cls, item) -> None:
        cls.relacao_contas_da_agencia.append(item)

    @property
    def limite(self):
        return self._limite

# ----------------------------------------------------------------
# MOCK
conta_teste = ContaCorrente('444','777-7','0001-9',0,0)
ContaCorrente.db_adicionar_conta(conta_teste)

conta_teste2 = ContaCorrente('444','999-7','0001-9',0,0)
ContaCorrente.db_adicionar_conta(conta_teste2)

conta_teste3 = ContaCorrente('444','888-5','0001-9',0,0)
ContaCorrente.db_adicionar_conta(conta_teste3)

conta_teste4 = ContaCorrente('444','822-5','0001-9',0,0)
ContaCorrente.db_adicionar_conta(conta_teste4)