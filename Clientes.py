from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime as dt
import servicos

relacao_clientes = []
relacao_cpf = []

class Clientes:
   
    def __init__ (self, endereco:str):
        self._endereco = endereco
        self._contas = []
       
               
    def adicionar_conta(self, conta):
        self._contas.append(conta)
 
    
    @property
    def contas(self):
        return self._contas
  
  
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

def adicionar_cliente(item):
    relacao_clientes.append(item)
    
def verificar_cliente_cpf(item):
    
    for i in relacao_clientes:
        if item == i.cpf:
            print("Cliente já cadastrado no banco de dados!!!")
            
            

if __name__ == '__main__':
    
    c1 = PessoaFisica('444','alpha','09/09/2000','casa a')
    c1.adicionar_conta('1010-9')
    c1.adicionar_conta('1233-6')
   
    
    adicionar_cliente(c1)
    
    c2 = PessoaFisica('884','bravo','09/09/2000','casa b')
    c2.adicionar_conta('1013-9')
    
    
    adicionar_cliente(c2)
    
    c3 = PessoaFisica('994','charlie','09/09/2000','casa c')
    c3.adicionar_conta('1220-1')
    
    
    adicionar_cliente(c3)
    
    c4 = PessoaFisica('744','delta','09/09/2000','casa d')
    c4.adicionar_conta('2310-4')
   
    
    
    adicionar_cliente(c4)
    
    verificar_cliente_cpf('444')
    
    
    for i in relacao_clientes:
        print(i.cpf, i.nome, i.contas, i.endereco)

    