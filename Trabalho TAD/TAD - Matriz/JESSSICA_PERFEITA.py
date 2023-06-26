from tadmatriz import *

arquivo = open("Trabalho TAD\TAD - Matriz\matops.txt","rt")
arq = arquivo.readline()


while arq != "":
    print(arq)
    # Fazer o split da linha obtida para uma lista
    linhaSplit = arq.split()

    # Definir variáveis para obter e salvar o resultado
    letraMatA = linhaSplit[0]
    operador = linhaSplit[1]
    letraMatB = linhaSplit[2]
    resultado = []
    

    if "T" in letraMatA and "-" in letraMatA:
        letraMatA = matA.replace("T","")
        letraMatA = matA.replace("-","")
        matA = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
        matA = transp_mat(matA)
        matA = neg_mat(matA)
    elif "T" in letraMatB and "-" in letraMatB:
        letraMatB = letraMatB.replace("T","")
        letraMatB = letraMatB.replace("-","")
        matB = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)
        matB = transp_mat(matB)
        matB = neg_mat(matB)
    else:
        if "T" in letraMatA or "-" in letraMatA:
            if "T" in letraMatA:
                letraMatA = letraMatA.replace("T","")
                matA = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
                matA = transp_mat(matA)

            if "-" in letraMatA:
                letraMatA = letraMatA.replace("-","") 
                matA = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
                matA = neg_mat(matA)
        else:
            matA = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
        if "T" in letraMatB or "-" in letraMatB:
            if "T" in letraMatB:
                letraMatB = letraMatB.replace("T","")
                matB = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)
                matB = transp_mat(matB)
            if "-" in letraMatB:
                letraMatB = letraMatB.replace("-","") 
                matB = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)
                matB = neg_mat(matB)
        else:
            matB = carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)

    # Obtenção dos resultados após realizar operações especificadas
    if operador=="+":
        resultado = soma_mat(matA, matB)
    if operador=="-":
        resultado = soma_mat(matA, neg_mat(matB))
    if operador=="x":
        resultado = multi_mat(matA, matB)
    
    if(resultado == None):
        print("Operação não conseguiu ser realizada.")
    else:
        print(f"Resultado: {resultado}")

    arq = arquivo.readline()
        