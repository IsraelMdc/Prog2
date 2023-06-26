from tadmatriz import *

arquivo = open("Trabalho TAD\TAD - Matriz\matops.txt","rt")
arq = arquivo.readline()
print(arq)
while arq != "":
    operacao = arq.split()
    print(operacao)
    matA = operacao[0]
    tadmatA = matA
    matB = operacao[2]
    tadmatB = matB
    print("mat A",matA)
    print("mat B",matB)
    print()
    operador = operacao[1]
##negativa mat
    if "-" in matA:
        print(matA)
        matA=matA.replace("-","")
        print(matA)
        print()
        tadmatA=carrega_mat("Trabalho TAD\\TAD - Matriz\\" + matA)
        print(tadmatA)
        tadmatA=neg_mat(tadmatA)
        print(tadmatA)
        print()

    if "-" in matB:
        print(matB)
        matB=matB.replace("-","")
        print(matB)
        print()
        tadmatB=carrega_mat("Trabalho TAD\\TAD - Matriz\\" + matB)
        print(tadmatB)
        tadmatB=neg_mat(tadmatB)
        print(tadmatB)
        print()
##
    if "T" in matA:
        print(matA)
        matA=matA.replace("T","")
        print(matA)
        print()
        tadmatA=carrega_mat("Trabalho TAD\\TAD - Matriz\\" + matA)
        print(tadmatA)
        tadmatB=transp_mat(tadmatA)
        print(tadmatA)
        print()     

    if "T" in matB:
        print(matB)
        matB=matB.replace("T","")
        print(matB)
        print()
        tadmatB=carrega_mat("Trabalho TAD\\TAD - Matriz\\" + matB)
        print(tadmatB)
        tadmatB=transp_mat(tadmatB)
        print(tadmatB)
        print()
    
    if operador=="+":
        tadC=soma_mat(tadmatA, tadmatB)
        print(tadC)
    if operador=="x":
        tadC=multi_mat(tadmatA, tadmatB)
        print(tadC)

    arq = arquivo.readline()
    print(arq)
        