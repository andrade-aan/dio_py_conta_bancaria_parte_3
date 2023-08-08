from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
# from Clientes import Clientes

class Cadastro:
    pass

class Clientes:
   
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = contas[]
    
    def realizar_transacao(self, conta, transacao):
        pass
    
    def adicionar_conta(self, conta):
        
        self._contas.append(conta)

class PessoaFisica(Clientes):
    
    def __init__(self,cpf:str, nome:str, data_nascimento:str):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')    
    pass

class PessoaJuridica(Clientes):
    pass

class Conta:
    
    pass
    