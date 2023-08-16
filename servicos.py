import datetime
import abc
import datetime as dt
import clientes, conta

conta_cliente_ag0001=0

class Servicos:
    
    @staticmethod
    def instante() -> datetime: # registrar data e hora de cada operação do sistema
        
        operacao_registro_hora = dt.datetime.now()
        reg_hora_operacao_formatado = operacao_registro_hora.strftime("%d/%m/%Y - %H:%M:%S")    
        
        return reg_hora_operacao_formatado
    
    @staticmethod
    def criar_conta() ->str: # apenas geracao do numero de conta
        
        global conta_cliente_ag0001
        
        conta_cliente_ag0001 +=1 
        digito = ((conta_cliente_ag0001-1)%9)
        numero_conta = str("10"+str(conta_cliente_ag0001)+"-"+str(digito))
        print(f'Conta n° {numero_conta} criada com sucesso!!!')

        return numero_conta
    
    @staticmethod
    def cadastrar_pessoa_fisica() -> list|bool:
        
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
        
        # enviar para transacoes.Cadastro como list       
        return cpf_titular_pf, nome_titular_pf, data_nascimento_pf, endereco_pf
    
    @staticmethod
    def tratar_cpf(cpf_digitado) -> str|bool:
        cpf_cliente = cpf_digitado
        #  tratamento para entrada CPF cliente
        tratamento = cpf_cliente.replace(" ", "")
        tratamento1 = tratamento.replace(".", "")
        cpf_cliente = tratamento1.replace("-", "")
        
        return cpf_cliente if cpf_cliente.isnumeric() else False
      
      
    @staticmethod    
    def verificar_data(entrada_data) -> str:
        
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
    
        
    @staticmethod
    def verificar_cliente_cpf(item) -> bool:
        
        for i in clientes.Clientes.relacao_clientes:
            
            if item == i.cpf:
                print("Cliente já cadastrado no banco de dados!!!")
                return True
        
        return False
    
    
    @staticmethod   # opção 3 do menu gerencia         
    def listar_clientes_pf() -> None:
        for i in clientes.Clientes.relacao_clientes:
            print(i.cpf, i.nome, i.contas, i.endereco)   
    
    
    @staticmethod
    def listar_contas_agencia() -> None:
        for i in conta.Conta.relacao_contas_da_agencia:
            print(i.cliente_cpf, i.numero_conta,
                 i.numero_agencia, i.saldo, i.limite)
    
    @staticmethod
    def identificar_cliente_conta() -> list|bool:
        
        cpf_cliente = str(input('\n\nDigite o CPF do titular da Conta: '+
                                '\n\n>>> '))
        
        verificacao_01 = Servicos.tratar_cpf(cpf_cliente)
        
        if verificacao_01 == False:
            print('CPF inválido!!!')
            return False
        
        verificacao_02 = Servicos.verificar_cliente_cpf(verificacao_01)
        
        if verificacao_02 == False:
            print('\nCPF informado não está cadastrado!!!')
            return False
         
        for i in conta.Conta.relacao_contas_da_agencia:
            
            if verificacao_01 == i.cliente_cpf:
                cpf_titular = i.cliente_cpf
                print(f'Conta Cadastrada: {i.numero_conta}')
        
        conta_cliente = str(input('\n\nDigite o numero da conta para realizar a operação: '+
                            '\n\n>>> '))
        
        for i in conta.Conta.relacao_contas_da_agencia:
            if conta_cliente == i.numero_conta:
                return i.cliente_cpf, i.numero_conta
        
        print('\n\nNúmero de conta inválido!!!')
    
    @staticmethod   
    def borda(texto) -> None:
        tam = len(texto)
        if tam:
            print('+','-'*tam,'+')
            print('|',texto,'|')
            print('+','-'*tam,'+')       
      
    # Método adicional para teste
    @staticmethod
    def validar_cpf(cpf) -> bool:
        
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
