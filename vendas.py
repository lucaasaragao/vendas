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

def add_func(funcionarios,codigo):
    nome=input("DIGITE O NOME DO FUNCIONARIO: \n")
    codigo=codigo+1
    funcionarios.append(nome,codigo)
    return cod_func
    
funcionarios=[]
cod_func=0
op=menu()
add_func(funcionarios,cod_func)
