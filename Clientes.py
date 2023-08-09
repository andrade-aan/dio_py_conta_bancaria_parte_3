from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime as dt


class Clientes:
   
    def __init__ (self, endereco:str):
        self._endereco = endereco
        self._contas = []
               
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
   # def __str__(self) -> str:
   #     return f'Endereço: {self._endereco}\nContas: {self._contas}'

class PessoaFisica(Clientes):
    
    def __init__(self, cpf:str, nome:str, data_nascimento:str, endereco:str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = dt.strptime(data_nascimento, '%d/%m/%Y')    
    
    def __repr__(self):
        return f'CPF: {self._cpf}\n'\
                f'Nome: {self._nome}\n'\
                f'Data de Nascimento: {self._data_nascimento}\n'\
                f'Endereço: {self._endereco}\n'\
                f'Contas: {self._contas}'


if __name__ == '__main__':
    
    c1 = PessoaFisica('444','a','09/09/2000','reu')
    c1.adicionar_conta('1010-9')
    print (c1)