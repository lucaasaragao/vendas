med_receitas="MedicamentosReceitas.txt"
from datetime import datetime
def menu():
    print("╔══════════════════════════════════════════════════════════╗")  
    print("║  1 - INSERIR NOVO FUNCIONARIO                            ║")                          
    print("║  2 - INSERIR MEDICAMENTOS                                ║")
    print("║  3 - VERIFICAR SE ESSE MEDICAMENTO NECESSITA DE RECEITA  ║")
    print("║  4 - ALTERAR ESTOQUE E RECEITA DO MEDICAMENTO            ║")
    print("║  5 - EXCLUIR MEDICAMENTO DO ESTOQUE                      ║")
    print("║  6 - SAIDA DE MEDICAMENTOS DO ESTOQUE                    ║")
    print("║  7 - RELATORIO DE SAIDA                                  ║")
    print("║  8 - QUANTIDADE DE MEDICAMENTOS EM ESTOQUE(RELATORIO)    ║")
    print("║  9 - SAIR                                                ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║                DIGITE A OPÇÃO DESEJADA                   ║")
    print("╚══════════════════════════════════════════════════════════╝")          
import time
import os
def cls():
    os.system("cls")
def porcentagem():
    for i in range (100):
        return i
import time
for i in range (50):
    print ("▓",end="")
    time.sleep(0.01)
print ("\nDream team agradece sua espera! ⌛")
time.sleep(1)
cls()

 
def add_func(funcionario,codigo):
    arq = open("Funcionarios.txt", "a")
    print("%s;%s" % (codigo,funcionario), file = arq)
    arq.close()
        
def add_medicamento(medicamento):
    arq = open ("Estoque.txt","a")
    print("%s;%s;%s" %(medicamento[0],medicamento[1],medicamento[2]), file = arq)
    arq.close()

def atualizar_medicamentos(medicamento):
    arq = open ("Estoque.txt","a")
    print("%s;%s;%s" %(medicamento[0],medicamento[1],medicamento[2]), file = arq)
    arq.close()
    
def ler_estoque():
    estoque=[]
    arq = open ("Estoque.txt","r")
    linhas = [linha.strip() for linha in arq]
    for linha in linhas:
        medicamento=linha.split(";")
        nome=medicamento[0]
        qt=medicamento[1]
        receita=medicamento[2]
        estoque.append([nome,qt,receita])
    return estoque

def verificacao(nome):
    arq = open ("Estoque.txt","r")
    linhas = [linha.strip() for linha in arq]
    for linha in linhas:
        medicamento=linha.split(";")
        if medicamento[0]==nome:
            return medicamento[2]
    arq.close()
    
def alterar(nome):
    arq = open ("Estoque.txt","r")
    linhas = arq.read().splitlines()
    for linha in linhas:
        medicamento=linha.split(";")
        if medicamento[0]==nome:
            deletar(nome)
            nova_quantia=input("QUAL A NOVA QUANTIA DO MEDICAMENTO ✎: ")
            medicamento[1]=nova_quantia
            nova_receita=input("ESTE MEDICAMENTO NECESSITA DE RECEITA:[S/N] ")
            if nova_receita=="s" or nova_receita=="S":
                nova_receita="SIM"
                medicamento[2]=nova_receita
            else:
                nova_receita="NAO"
                medicamento[2]=nova_receita
        add_medicamento(medicamento)
    arq.close()

def deletar(nome):
    estoque=ler_estoque()
    for i,medicamento in enumerate(estoque):
        if medicamento[0]==nome:
            estoque.pop(i)
    arq = open ("Estoque.txt","w")
    print("",end="")
    arq.close()
    for i in estoque:
        atualizar_medicamentos(i)

def verificar_qt_estoque(nome):
    estoque=ler_estoque()
    for medicamento in estoque:
        if medicamento[0]==nome:
            return medicamento[1]

def alterar_estoque(nome,qt):
    estoque=ler_estoque()
    for medicamento in estoque:
        if medicamento[0]==nome:
            medicamento[1]=int(medicamento[1])-qt
    arq = open ("Estoque.txt","w")
    print("",end="")
    arq.close()
    for i in estoque:
        atualizar_medicamentos(i)
  
def saida_do_estoque():
    cod_func=input("DIGITE O CODIGO DO VENDEDOR:✎\n")
    remedio=input("DIGITE O NOME DO REMEDIO:✎\n")
    qt_saiu=int(input ("DIGITE A QUANTIDADE DE REMEDIOS A SEREM VENDIDOS:✎\n"))
    qt=int(verificar_qt_estoque(remedio))
    if qt>0 and qt<qt_saiu:
        print("SÓ EXISTEM %s REMEDIOS NO ESTOQUE!\n"%qt)
        print("QUANTIDADE DE REMEDIOS NO ESTOQUE ESTÁ ABAIXO DO NECESSARIO PARA REALIZAR ESTA VENDA!☹")
    elif qt==0:
        print("ESTE REMEDIO ESTA EM FALTA NO ESTOQUE ✘")
    else:
        alterar_estoque(remedio,qt_saiu)
        gerador_relatorio_saida(cod_func,remedio,qt_saiu)

def checar_funcionario(cod_func):
    arq = open ("Funcionarios.txt","r")
    linhas = [linha.strip() for linha in arq]
    for linha in linhas:
        funcionario=linha.split(";")
        if funcionario[0]==cod_func:
            return funcionario[1]


def gerador_relatorio_saida(cod_func,nome_remedio,qt):
    arq = open ("RelatorioSaidas.txt", "a")
    nome=checar_funcionario(cod_func)
    hora=datetime.today()
    print("%s;%s;%s;%s;%s"%(cod_func,nome,nome_remedio,qt,hora), file = arq)
    print("RELATORIO GERADO COM SUCESSO ⌛ ")
    arq.close() 
        
def exibir_relatorio():
    print ("************** RELATORIO DE CADA SAIDA ******************")
    arq = open ("RelatorioSaidas.txt","r")
    linhas = [linha.strip() for linha in arq]
    for linha in linhas:
        saida=linha.split(";")
        print("         CODIGO FUNCIONARIO: ",saida[0])
        print("         NOME DO FUNCIONARIO: ",saida[1])
        print("         REMEDIO RETIRADO: ",saida[2])
        print("         QUANTIDADE: ",saida[3])
        print("         HORA: ",saida[4])
        print("*"*60)
        
def relatorio_de_estoque():
    arq = open ("Estoque.txt","r")
    linhas = [linha.strip() for linha in arq]
    for linha in linhas:
        medicamento=linha.split(";")
        print("         NOME DO REMEDIO: ",medicamento[0])
        print("         QUANTIDADE EM ESTOQUE: ",medicamento[1])
        print("         NECESSITA DE RECEITA: ",medicamento[2])
        print("-"*60)

















