from datetime import datetime as dt

conta_cliente_ag0001=0

class Servicos:
    
    def instante(): # registrar data e hora de cada operação do sistema
        
        operacao_registro_hora = dt.now()
        reg_hora_operacao_formatado = operacao_registro_hora.strftime("%d/%m/%Y - %H:%M:%S")    
        
        return reg_hora_operacao_formatado
    
    def criar_conta():
        
        global conta_cliente_ag0001
        
        conta_cliente_ag0001 +=1 
        digito = ((conta_cliente_ag0001-1)%9)
        numero_conta = str("10"+str(conta_cliente_ag0001)+"-"+str(digito))

        return numero_conta
    
    def cadastrar_pessoa_fisica():
        
        nome_titular_pf = input("Digite o nome completo: ")
        cpf_titular_dig = input("Digite o CPF: ")
        cpf_titular_pf = Servicos.tratar_cpf(cpf_titular_dig)
        data_nascimento_pf = input("Digite a data de nascimento 'dd/mm/aaaa': ")
        
        return nome_titular_pf, cpf_titular_pf, data_nascimento_pf
    
    def tratar_cpf(cpf_digitado):
        cpf_cliente = cpf_digitado
        #  tratamento para entrada CPF cliente
        tratamento = cpf_cliente.replace(" ", "")
        tratamento1 = tratamento.replace(".", "")
        cpf_cliente = tratamento1.replace("-", "")
    
        return cpf_cliente



if __name__ == "__main__":
    a = Servicos.instante()
    print(a)
    e = Servicos.criar_conta()
    r = Servicos.criar_conta()
    w = Servicos.criar_conta()
    print(w, r, e)
    pf = Servicos.cadastrar_pessoa_fisica()
    print(pf)