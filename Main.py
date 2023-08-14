import clientes, servicos, conta, historico, transacoes


def menu_principal():
    print("\n1 - SACAR")
    print("2 - DEPOSITAR")
    print("3 - EXTRATO")
    print("4 - SALDO")
    print("5 - GERENCIA")
    print("99 - SAIR")        


def menu_gerencia():
    
    while True:
        
        # adicionar simulação de usuario/senha na versão final
        servicos.Servicos.borda("Menu de Gerência Agência 0001 - Bem-vindo!")
        
        print(servicos.Servicos.instante())
        print("\n1 - CADASTRAR NOVA CONTA")
        print("2 - CADASTRAR CLIENTE")
        print("3 - LISTAR CLIENTES")
        print("99 - SAIR")
        
        opcao = str(input("\n\nDigite a opção desejada:" +
                        "\n\n>>> "))
        
        if opcao == '1':
            
            servicos.Servicos.instante()
            cpf_titular_dig = str(input("Digite o CPF do cliente: "))
            
            cpf_titular_pf = servicos.Servicos.tratar_cpf(cpf_titular_dig)
        
            if cpf_titular_pf == False:
                print('CPF digitado não é válido!!!')
                return False
        
            verificacao_bs_dados = servicos.Servicos.verificar_cliente_cpf(cpf_titular_pf)
            if verificacao_bs_dados:
                transacoes.Cadastro.criar_nova_conta_cliente(cpf_titular_pf)
                
            else:
                print('CPF não cadastrado como cliente!!!')
        
        elif opcao == '2':
            servicos.Servicos.instante()
            transacoes.Cadastro.criar_novo_cliente()
        
        elif opcao == '3':
            servicos.Servicos.instante()
            servicos.Servicos.listar_clientes_pf()  
        
        elif opcao == '99':
            print("\n\n")
            break
            
        else:
            print("\n\nOpção Inválida!!")
                
            
            
#Main function    

while True:
    
    print("\n")
    servicos.Servicos.borda("Bem-vindo a sua conta corrente")
    
    print(servicos.Servicos.instante())        
    menu_principal()
    
    
    opcao = str(input("\n\nDigite a opção desejada:" +
                      "\n\n>>> "))
    
    
    # implementar operação de saque
    if opcao == '1':...
        
        #sacar()
    
    # implementar operação de deposito   
    elif opcao == '2':...
        
        # depositar()
    
    
    # implementar operação de extrato        
    elif opcao == '3':
        
        servicos.Servicos.borda("EXTRATO - CONTA CORRENTE")
                
        conta_cliente=str(input("\nDigite a conta para Emissão de Extrato: "))
        
        controle = False
        
    # implementar operação de saldo       
    elif opcao == '4':
        
        controle = False
        
        
    elif opcao == '5':
        menu_gerencia()    
        
    elif opcao == '99':
        print("\n\n")
        servicos.Servicos.borda("Obrigado por utilizar nossos serviços!!! Aplicativo Finalizado...")
        break
        
    else:
        print("\n\nOpção Inválida!!")