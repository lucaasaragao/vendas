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


def add_func():
    arq= open("Cadastro.txt", "a")
    funcionario=input("DIGITE SEU NOME: ")
    codigo=int(input("DIGITE SEU CODIGO: "))
    print("%s;%s" % (codigo,funcionario), file = arq)
    arq.close()


def leitura_func():
    arq = open("Cadastro.txt", "r")
    funcionarios = arq.readlines()
    for funcionario in funcionarios:
        func = funcionario.split(";")
        cod = func[0]
        nome = func[1]
        print(cod,nome)
    arq.close()

'''
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
'''

while continua:
    opcao = menu()
    if opcao == "1":
        #blah balh
    # ...
