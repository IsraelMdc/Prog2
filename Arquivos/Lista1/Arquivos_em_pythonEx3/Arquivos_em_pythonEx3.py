# 3. Um arquivo chamado dadosmat.txt armazena o conteúdo de uma matriz de floats de 10 linhas por 5 colunas (10x5).
# No arquivo, cada linha contém apenas 1 elemento da matriz.
# Construa um programa python que realize o seguinte processamento sobre o arquivo dadosmat.txt:
 
# a) Leia o conteúdo do arquivo uma linha por vez e armazene os dados em uma matriz do tipo lista de listas;
# b) Salve o conteúdo da matriz em um arquivo de saída chamado mat10x5.txt. Neste
# arquivo, os dados devem estar organizados no formato matricial. 
# Veja o modelo exemplo a seguir (matriz 2x3):
#  Arquivo dadosmat.txt:             Arquivo mat2x3.txt
#     12                                  12 5 2
#     5                                   7 23 4
#     2
#     7
#     23
#     4

input_arq_dados = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Arquivos\\Arquivos_em_pythonEx3\\dadosmat.txt"
output_arq = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Arquivos\\Arquivos_em_pythonEx3\\mat2x3.txt"
arquivos_dados = open(f"{input_arq_dados}", "rt")
lista = []
matriz = []
for linha in arquivos_dados:
    if linha[-1] == "\n":
        elemento = linha[:-1]
    else:
        elemento = linha
    lista.append(elemento)
print(lista)

for k in range(len(lista)):
    lista[k] = int(lista[k]) 

print(lista)

list_aux=[]
for i in range(len(lista)):
    list_aux.append(lista[i])
    if len(list_aux) == 3:
        matriz.append(list_aux)
        list_aux = []
print(matriz)
print(len(matriz))
print(matriz[0])

arquivo_processado = open(f"{output_arq}","wt")
for i in range(len(matriz)):
    print(type(matriz[i]))
    arquivo_processado.write(str(matriz[i])+ '\n')
arquivo_processado.close()


