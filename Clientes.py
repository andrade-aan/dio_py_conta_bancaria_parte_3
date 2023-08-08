from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime as dt


class Clientes:
   
    def __init__ (self, endereco:str):
        self._endereco = endereco
        self._contas = []
        
       
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def __str__(self) -> str:
        return f'Endereço: {self._endereco}\nContas: {self._contas}'

class PessoaFisica(Clientes):
    
    def __init__(self,cpf:str, nome:str, data_nascimento:str, endereco:str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = dt.strptime(data_nascimento, '%d/%m/%Y')    




if __name__ == '__main__':
    
    c1 = PessoaFisica('444','a','09/09/2000','reu')
    c1.adicionar_conta('01-1')
    print (c1)