from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime as dt
import servicos


class Clientes:
   
    def __init__ (self, endereco:str):
        self._endereco = endereco
        self._contas = []
               
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
    
    def listar(self, cpf):
        resultados = [i for i in self._cpf]
        
    
    
    
if __name__ == '__main__':
    
    c1 = PessoaFisica('444','alpha','09/09/2000','casa a')
    c1.adicionar_conta('1010-9')
    
    c2 = PessoaFisica('884','bravo','09/09/2000','casa b')
    c3 = PessoaFisica('994','charlie','09/09/2000','casa c')
    c4 = PessoaFisica('744','delta','09/09/2000','casa d')
    a = [PessoaFisica.cpf]
    print(getattr(c4,'cpf'))
    
    print(c3.__dict__, c2.__dict__, c1.__dict__)
    

    