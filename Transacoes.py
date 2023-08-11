from abc import ABC, abstractmethod
from datetime import datetime as dt
import servicos
import clientes


class Transacoes(ABC):
    
    def debito(self):...

class Cadastro:
    
    def criar_cliente():
        dados_cliente = servicos.Servicos.cadastrar_pessoa_fisica()
        consultar_cliente = servicos.Servicos.verificar_existencia_cliente(dados_cliente[0])
        novo_cliente = clientes.PessoaFisica(dados_cliente[0], 
                                             dados_cliente[1],
                                             dados_cliente[2],
                                             dados_cliente[3])
        
        
        
        return novo_cliente
        
        
        
if __name__ == '__main__':
    c1 = clientes.PessoaFisica('444','a','09/09/2000','reu')
    c2 = clientes.PessoaFisica('884','b','09/09/2000','reu')
    c3 = clientes.PessoaFisica('994','c','09/09/2000','reu')
    c4 = clientes.PessoaFisica('744','d','09/09/2000','reu')
    
    a = Cadastro.criar_cliente()
    print(a)
    