

# criação de padronização de registro de histórico para movimentação em conta

class Historico:
    
    def __init__(self, codigo_transacao:str|None=None, 
                 descricao_historico: str|None=None):
        self.__codigo_transacao = codigo_transacao
        self.__descricao_historico = descricao_historico
        self.__historico_transacoes = {'101': 'DEPÓSITO',
                                       '201':'SAQUE',
                                       '001':'ABERTURA DE CONTA',
                                       '999':'ENCERRAMENTO DE CONTA',
                                       '211': 'DÉBITO EM CONTA',
                                       '111': 'CRÉDITO EM CONTA',
                                       '010':'RECEBIMENTO PROVENTOS/REMUNERAÇÃO'}
    
   
    def selecionar_transacao(self, codigo_transacao):
        
        for key, value in self.__historico_transacoes.items():
            if key == codigo_transacao:
                return value
    
    
    def registrar_transacao(self) -> None:...
    
    
if __name__ == '__main__':
    historico = Historico()
    print(historico.selecionar_transacao('101'))
    
    
        