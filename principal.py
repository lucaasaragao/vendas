import arquivos
continua="True"
medicamento=[]
while continua:
    arquivos.menu()
    opcao = input( "☛ ")
    if opcao == "1":
        print("*"*60)
        funcionario=input("DIGITE O NOME DO VENDEDOR ✎: ")
        codigo_funcionario=input("DIGITE O CODIGO DO VENDEDOR ✎: ")
        arquivos.add_func(funcionario,codigo_funcionario)
        print("FUNCIONARIO CADASTRADO COM CODIGO %s" %codigo_funcionario)
        print("*"*60)
    if opcao == "2":
        print("*"*60)
        remedio=input("DIGITE O NOME DO REMEDIO QUE DESEJA CADASTRAR ✎: ")
        quantidade=input("DIGITE A QUANTIDADE DISPONIVEL ✎: ")
        receita=input("ESTE MEDICAMENTO NECESSITA DE RECEITA:[S/N] ")
        if receita=="s" or receita=="S":
            receita="SIM"
        else:
            receita="NAO"
        medicamento=remedio,quantidade,receita
        arquivos.add_medicamento(medicamento)
        print("*"*60)
    if opcao == "3":
        print("*"*60)
        remedio=input("DIGITE O NOME DO REMEDIO QUE DESEJA VERIFICAR: ")
        resposta=arquivos.verificacao(remedio)
        if resposta=="SIM":
            print("ESTE MEDICAMENTO PRECISA DE RECEITA!✔\n\n")
        else:
            print("ESTE MEDICAMENTO NÃO PRECISA DE RECEITA!✘\n\n")
        print("*"*60)
    if opcao == "4":
        print("*"*60)
        remedio=input("QUAL REMEDIO VOCÊ DESEJA ALTERAR ⟲: ")
        arquivos.alterar(remedio)
        print("*"*60)
    if opcao == "5":
        print("*"*60)
        remedio=input("QUAL REMEDIO DESEJA EXCLUIR DO ESTOQUE ✂: ")
        arquivos.deletar(remedio)
        print("REMEDIO EXCLUIDO COM SUCESSO!✔")
        print("*"*60)
    if opcao == "6":
        print("*"*60)
        arquivos.saida_do_estoque()
        print("*"*60)
    if opcao == "7":
        arquivos.exibir_relatorio()
    if opcao == "8":
        print("*"*60)
        arquivos.relatorio_de_estoque()
        print("*"*60)
    if opcao == "9":
        print("*"*60)
        print ("ATÉ LOGO!")
        print("Dream team software")
        print("☎   9.9941-3959", "✉ dreamteam.com.br")
        print("*"*60)
        continua=False
    

        
