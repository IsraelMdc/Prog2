def cria_mat(qlinhas, qcolunas):
    lst=[]
    tadmat=[]
    for linha in range(qlinhas):
        for coluna in range(qcolunas):
            lst.append(0)
        tadmat.append(lst)
        lst=[]

    return tadmat
    
def multi_mat(tadA, tadB):
    if len(tadA[0]) == len(tadB):
        tadmatx=cria_mat(len(tadA), len(tadB[0]))
        for linha in range(len(tadA)):
            for coluna in range(len(tadB[linha])):
                for coluna2 in range(len(tadA[linha])):
                    tadmatx[linha][coluna]+=tadA[linha][coluna2]*tadB[coluna2][coluna]

        return tadmatx
    else:
        return None
        
def neg_mat(tadA):
    for linha in range(len(tadA)):
        for coluna in range(len(tadA[linha])):
            tadA[linha][coluna]=tadA[linha][coluna]*-1
      
    return tadA   

def soma_mat(tadA, tadB):
    if (len(tadA) == len(tadB)) and len(tadA[0]) == len(tadB[0]):
        lst_out=cria_mat(len(tadA), len(tadA[0]))
        for linha in range(len(tadA)):
            for coluna in range(len(tadA[linha])):
                lst_out[linha][coluna]=tadA[linha][coluna]+tadB[linha][coluna]
        return lst_out
    else:
        return None
    
def  transp_mat(tadA):
    tadTA=cria_mat(len(tadA[0]), len(tadA))
    for linha in range(len(tadA)):
        for coluna in range(len(tadA[linha])):
            tadTA[coluna][linha]=tadA[linha][coluna]
    return tadTA
  
def carrega_mat(nomearq):
    nomearq+=".txt"
    arquivo = open(nomearq , 'rt')
    lista = []
    linha = arquivo.readline()
    
    while linha != "":
        linhatratada = linha.strip().split('    ')
        for i in range(len(linhatratada)):
            linhatratada[i] = int(linhatratada[i])
        lista.append(linhatratada)
        linha = arquivo.readline()   
    arquivo.close()
    return lista  
    
def salvamat(tadmat,nomearq):
    arq = open(nomearq,"wt")

    matriz_saida = ""
    for i in range(len(tadmat)):
        for j in range(len(tadmat[i])):
            matriz_saida += (f"{tadmat[i][j]:>6}")
        matriz_saida += '\n'
        
    arq.write(f"{matriz_saida}")
    arq.close()
    return tadmat
    