# Dois arquivos chamados matA5x10.txt e matB5x10.txt contém, respectivamente, duas matrizes de inteiros de dimensões 5 x 10.
# O formato dos arquivos é aquele onde cada linha do arquivo representa uma linha da matriz. 
# Sabendo disso, faça o que é pedido a seguir:
# b) No mesmo programa python do item anterior, escreva a função salvamat(nomearq,m).
# Esta função recebe como primeiro parâmetro de entrada um nome de arquivo. A função
# deve usar o parâmetro para nomear e abrir um arquivo texto para escrita. Em seguida, a
# função deve escrever no arquivo os dados da matriz m passada como segundo
# parâmetro. Cada linha do arquivo deve conter uma linha da matriz. Por último, a função
# fecha o arquivo e retorna a matriz m.
# c) No mesmo programa python do item anterior, escreva a função somaMat(ma,mb). Esta
# função recebe como parâmetros de entrada 2 matrizes de ints. A função devolve uma
# terceira matriz contendo a soma das duas matrizes de entrada. Pesquise na internet a
# regra para a soma de matrizes.
# d) Construa uma função main que utiliza as funções em a), b) e c) para carregar, somar e
# salvar o resultado da soma das matrizes nos arquivos matA5x10.txt e matB5x10.txt.
# Esses dois arquivos são fornecidos como material da tarefa.
# O arquivo de saída deve ser nomeado soma5x10.txt.
# Atenção: o programa deve estar apto a processar outros arquivos de matrizes e não
# somente os arquivos matA5x10.txt e matB5x10.txt.

arquivoA = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Arquivos\\Atividade_avaliativa\matA5x10.txt"
arquivoB = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Arquivos\\Atividade_avaliativa\matA5x10.txt"
matrizA = []
matrizB =  []

# a) Construa um programa python contendo uma função chamada loadmat(nomearq).
# Esta função recebe como parâmetro de entrada o nome de um arquivo texto qualquer contendo uma matriz 5 x 10.
# A função abre o arquivo, lê o seu conteúdo linha a linha e cria uma matriz python de inteiros (lista de listas).
# Por último, a função fecha o arquivo e retorna a matriz construída.

def loadmat(nomearq):
    arquivo = open(nomearq , 'rt')
    linha = arquivo.readline()
    
    matriz = []
    lista = []    

    while linha != "":
        # print(linhatratada)
        linhatratada = linha.strip().split(' ')
        print(linhatratada)
        # for i in range(len(linhatratada)):
        #     #linhatratada[i] = int(linhatratada[i])
        #     lista.append(linhatratada[i])
        #     print(lista)
        # matriz.append(lista)
        # linha = arquivo.readline()
        

    # matriz = []
    # for i in range(5):
    #     for j in range(10):
    #         matriz.append(nomearq.readline())

def main():
    loadmat(arquivoA)

if __name__ == '__main__':
    main()


