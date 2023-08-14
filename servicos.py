import abc
import datetime as dt
import clientes, conta

conta_cliente_ag0001=0

class Servicos:
    
    
    def instante(): # registrar data e hora de cada operação do sistema
        
        operacao_registro_hora = dt.datetime.now()
        reg_hora_operacao_formatado = operacao_registro_hora.strftime("%d/%m/%Y - %H:%M:%S")    
        
        return reg_hora_operacao_formatado
    
    
    def criar_conta():
        
        global conta_cliente_ag0001
        
        conta_cliente_ag0001 +=1 
        digito = ((conta_cliente_ag0001-1)%9)
        numero_conta = str("10"+str(conta_cliente_ag0001)+"-"+str(digito))

        return numero_conta
    
    
    def cadastrar_pessoa_fisica():
        
        cpf_titular_dig = str(input("Digite o CPF: "))
        cpf_titular_pf = Servicos.tratar_cpf(cpf_titular_dig)
        if cpf_titular_pf == False:
            print('CPF digitado não é válido!!!')
            return False
        
        verificacao_bs_dados = Servicos.verificar_cliente_cpf(cpf_titular_pf)
        
        if verificacao_bs_dados == True:
            return False
        
        
        
        nome_titular_pf = input("Digite o nome completo: ")
        
        data_nascimento_dig = input("Digite a data de nascimento 'dd/mm/aaaa': ")
        data_nascimento_pf = Servicos.verificar_data(data_nascimento_dig)
        if data_nascimento_pf == False:
            print('Data de nascimento digitada não é válida!!!')
            return False
        
        endereco_pf = str(input("Digite o endereço: "))
                
        return cpf_titular_pf, nome_titular_pf, data_nascimento_pf, endereco_pf
    
    @staticmethod
    def tratar_cpf(cpf_digitado):
        cpf_cliente = cpf_digitado
        #  tratamento para entrada CPF cliente
        tratamento = cpf_cliente.replace(" ", "")
        tratamento1 = tratamento.replace(".", "")
        cpf_cliente = tratamento1.replace("-", "")
        
        return cpf_cliente if cpf_cliente.isnumeric() else False
      
    @staticmethod    
    def verificar_data(entrada_data):
        
        data_atual = dt.date.today()
        
        try:
             dia, mes, ano = entrada_data.split("/")
             data1 = dt.date(day=int(dia), month=int(mes), year=int(ano))#.strftime("%d/%m/%Y")
        
        except Exception:
            print(f'Verifique Formato de data: dd/mm/aaaa !!\n'\
                  f'Data informada = {entrada_data}')
            return False
                
        dias_vida = data_atual - data1
        dias_no_ano = 365.2425
        dias_vida = int((data_atual - data1).days/dias_no_ano)
        
      
        # verificar tempo de vida 
        if dias_vida > 99 and dias_vida <= 120:
            resposta_dias_vida = str(input('Confirma idade superior a 100 anos? (s/n)'))
            return False if resposta_dias_vida == 'n' else entrada_data
        elif dias_vida > 120:
            print("Data Incorreta - tempo de vida superior a 120 anos!!")
            return False
        elif dias_vida <= 0:
            print("Data Incorreta - data informada é futura!!")
            return False
               
        return entrada_data
    
    def adicionar_cliente(item):
        clientes.relacao_clientes.append(item)
    
    @staticmethod
    def verificar_cliente_cpf(item) -> bool:
        
        for i in clientes.Clientes.relacao_clientes:
            print('passagem linha_105_servicos')
            if item == i.cpf:
                print("Cliente já cadastrado no banco de dados!!!")
                return True
        
        return False
    @staticmethod            
    def listar_clientes_pf():
        for i in clientes.Clientes.relacao_clientes:
            print(i.cpf, i.nome, i.contas, i.endereco)   
    
    
    
    # Método adicional para teste
    @staticmethod
    def validar_cpf(cpf):
        
        verificar_cpf = Servicos.tratar_cpf(cpf)
        
        if len(verificar_cpf) != 11:
            print('CPF digitado não é válido!!!')
            return False
        
        f:int = 0
        soma:int = 0
        for i in verificar_cpf[0:9]:
            i=int(i)
            digito_mult = (i*(10-f))
            f+=1
            soma+=digito_mult
        
        digito_dezena = ((soma*10)%11) 
        
        f:int = 0
        soma:int = 0
        
        for i in verificar_cpf[0:10]:
            i=int(i)
            digito_mult = (i*(11-f))
            f+=1
            soma+=digito_mult

        digito_unidade = ((soma*10)%11)
        
        print (digito_dezena, digito_unidade)
        
        unidade = int(verificar_cpf[10])
        dezena = int(verificar_cpf[9])
        
        if digito_dezena != dezena and digito_unidade != unidade:
            print('CPF digitado não é válido!!!')
            return False
        else:
            print('CPF válido!!!')
            True

    @staticmethod   
    def borda(texto):
        tam = len(texto)
        if tam:
            print('+','-'*tam,'+')
            print('|',texto,'|')
            print('+','-'*tam,'+')       
            
    
