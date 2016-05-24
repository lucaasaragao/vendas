def menu():
    print("1  - INSERIR NOVO FUNCIONARIO")
    print("2  - INSERIR MEDICAMENTOS")
    print("3  - VERIFICAR SE ESSE MEDICAMENTO NECESSITA DE RECEITA")
    print("4  - ALTERAR STATUS DE RECEITA DO MEDICAMENTO")
    print("5  - VERIFICAR ESTOQUE DO MEDICAMENTO")
    print("6  - ATUALIZAR ESTOQUE")
    print("7  - REALIZAR NOVA VENDA")
    print("8  - VENDEDOR QUE MAIS REALIZOU VENDAS")
    print("10 - SAIR")
    op=input("DIGITE SUA OPÇÃO: \n")
    return op

def add_func():
    arq= open("Cdastro.txt", "a")
    funcionario=input("DIGITE SEU NOME: ")
    codigo=int(input("DIGITE SEU CODIGO: "))
    print(funcionario, file = arq)
    print(codigo, file = arq)
    arq.close()

(add_func())
