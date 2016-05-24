def menu():
    print("1 - INSERIR NOVO FUNCIONARIO")
    print("2 - INSERIR MEDICAMENTOS")
    print("3 - VERIFICAR SE ESSE MEDICAMENTO NECESSITA DE RECEITA")
    print("4 - ALTERAR STATUS DE RECEITA DO MEDICAMENTO")
    print("5 - VERIFICAR ESTOQUE DO MEDICAMENTO")
    print("6 - ATUALIZAR ESTOQUE")
    print("7 - REALIZAR NOVA VENDA")
    print("8 - VENDEDOR QUE MAIS REALIZOU VENDAS")
    print("10 - SAIR")
    op=input("DIGITE SUA OPÇÃO: \n")
    return op

(menu())
#-------------------------------------------------------------------
def add_func():
    arq= open("Cadastro.txt", "a")
    funcionario=input("DIGITE SEU NOME: ")
    codigo=int(input("DIGITE SEU CODIGO: "))
    print(funcionario, file = arq)
    print(codigo, file = arq)
    arq.close()

(add_func())

#----------------------------------------------------------------------
def leitura_func():
    arq = open("Cadastro.txt", "r")
    funcionario = arq.read()
    codigo = arq.read()
    print(funcionario)
    print(codigo)
    arq.close()

#-----------------------------------------------------------------------
def add_med():
    arq= open("Estoque.txt", "a")
    medicamento=input("DIGITE O MEDICAMENTO: ")
    receita=input("ESSE MEDICAMNTO PRECISA DE RECEITA ? [S/N]")
    if receita == "s" or receita == "S":
        arq=open("MedicamentosReceitas.txt", "a")
        print(medicamento, file = arq)
        print("MEDICAMENTO ADICIONADO)
    else:
        print("MEDICAMENTO ADICIONADO)

(add_med())
    
