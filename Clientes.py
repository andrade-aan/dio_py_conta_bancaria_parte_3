from abc import ABC
from datetime import datetime as dt
import servicos


class Clientes:
   
    relacao_clientes = []
   
    def __init__ (self, endereco:str):
        self._endereco = endereco
        self._contas = []
       
        
    @property
    def contas(self):
        return self._contas
    
    @classmethod
    def db_adicionar_clientes(cls, item):
        cls.relacao_clientes.append(item)
      
    def adicionar_conta(self, conta):
        self._contas.append(conta) 
  
class PessoaFisica(Clientes):
    
    def __init__(self, cpf:str, nome:str, data_nascimento:str, endereco:str):
        
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco)  
        

      
    def __repr__(self):
        return f'CPF: {self._cpf}\n'\
                f'Nome: {self._nome}\n'\
                f'Data de Nascimento: {self._data_nascimento}\n'\
                f'Endereço: {self._endereco}\n'\
                f'Contas: {self._contas}'
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def contas(self):
        return self._contas

    @property
    def endereco(self):
        return self._endereco

         


if __name__ == '__main__':
    
    c1 = PessoaFisica('444','a','09/09/2000','apto 12')
    c2 = PessoaFisica('884','b','09/09/2000','apto 39')
    c3 = PessoaFisica('994','c','09/09/2000','apto 45')
    c4 = PessoaFisica('744','d','09/09/2000','apto 11')
    
    c1.adicionar_conta('1111')
    
    Clientes.db_adicionar_clientes(c1)
    
    