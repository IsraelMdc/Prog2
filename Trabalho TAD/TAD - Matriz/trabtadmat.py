import tadmatriz as tadm

arquivo = open("Trabalho TAD\TAD - Matriz\matops.txt","rt")
arq = arquivo.readline()


while arq != "":
    # Fazer o split da linha obtida para uma lista
    linhaSplit = arq.split()

    # Definir variáveis para obter e salvar o resultado
    letraMatA = linhaSplit[0]
    matriz1 = letraMatA
    operador = linhaSplit[1]
    letraMatB = linhaSplit[2]
    matriz2 = letraMatB
    resultado = []
    

    if "T" in letraMatA and "-" in letraMatA:
        letraMatA = matA.replace("T","")
        letraMatA = matA.replace("-","")
        matA = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
        matA = tadm.transp_mat(matA)
        matA = tadm.neg_mat(matA)
        matriz1 = f"menos{letraMatA}"
    elif "T" in letraMatB and "-" in letraMatB:
        letraMatB = letraMatB.replace("T","")
        letraMatB = letraMatB.replace("-","")
        matB = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)
        matB = tadm.transp_mat(matB)
        matB = tadm.neg_mat(matB)
        matriz2 = f"menos{letraMatB}"
    else:
        if "T" in letraMatA or "-" in letraMatA:
            if "T" in letraMatA:
                letraMatA = letraMatA.replace("T","")
                matA = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
                matA = tadm.transp_mat(matA)
                matriz1 = f"transp{letraMatA}"

            if "-" in letraMatA:
                letraMatA = letraMatA.replace("-","") 
                matA = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
                matA = tadm.neg_mat(matA)
                matriz1 = f"menos{letraMatA}"
        else:
            matA = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatA)
        if "T" in letraMatB or "-" in letraMatB:
            if "T" in letraMatB:
                letraMatB = letraMatB.replace("T","")
                matB = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)
                matB = tadm.transp_mat(matB)
                matriz2 = f"transp{letraMatB}"
            if "-" in letraMatB:
                letraMatB = letraMatB.replace("-","") 
                matB = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)
                matB = tadm.neg_mat(matB)
                matriz2 = f"menos{letraMatB}"
        else:
            matB = tadm.carrega_mat("Trabalho TAD\\TAD - Matriz\\" + letraMatB)

    # Obtenção dos resultados após realizar operações especificadas
    if operador=="+":
        resultado = tadm.soma_mat(matA, matB)
        operador= "mais"
    if operador=="-":
        resultado = tadm.soma_mat(matA, tadm.neg_mat(matB))
        operador= "menos"
    if operador=="x":
        resultado = tadm.multi_mat(matA, matB)
        operador = "vezes"

    if(resultado == None):
        print("Operação não conseguiu ser realizada.")
    
    outdir = f"{matriz1+operador+matriz2}.txt"
    tadm.salvamat(resultado,outdir)
    arq = arquivo.readline()
        