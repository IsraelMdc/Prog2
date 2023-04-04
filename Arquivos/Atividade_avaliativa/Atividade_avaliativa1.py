# Dois arquivos chamados matA5x10.txt e matB5x10.txt contém, respectivamente, duas matrizes de inteiros de dimensões 5 x 10.
# O formato dos arquivos é aquele onde cada linha do arquivo representa uma linha da matriz. 
# Sabendo disso, faça o que é pedido a seguir:
# Atenção: o programa deve estar apto a processar outros arquivos de matrizes e não
# somente os arquivos matA5x10.txt e matB5x10.txt.

arquivoA = "Arquivos\Atividade_avaliativa\matA5x10.txt"
arquivoB = "Arquivos\Atividade_avaliativa\matB5x10.txt"
arquivoSaida = "Arquivos\Atividade_avaliativa\soma5x10.txt"

# a) Construa um programa python contendo uma função chamada loadmat(nomearq).
# Esta função recebe como parâmetro de entrada o nome de um arquivo texto qualquer contendo uma matriz 5 x 10.
# A função abre o arquivo, lê o seu conteúdo linha a linha e cria uma matriz python de inteiros (lista de listas).
# Por último, a função fecha o arquivo e retorna a matriz construída.

def loadmat(nomearq):
    arquivo = open(f'{nomearq}' , 'rt')
    linha = arquivo.readline()
    lista = []    

    while linha != "":
        linhatratada = linha.strip().split('    ')
        for i in range(len(linhatratada)):
            linhatratada[i] = int(linhatratada[i])        
        lista.append(linhatratada)

        print(f"{linhatratada}, Linha adicionada a matriz")
        linha = arquivo.readline()
    arquivo.close()
    print(f"matriz completa: {lista}")
    return lista

# b) No mesmo programa python do item anterior, escreva a função salvamat(nomearq,m).
# Esta função recebe como primeiro parâmetro de entrada um nome de arquivo.
#  A função deve usar o parâmetro para nomear e abrir um arquivo texto para escrita. 
# Em seguida, a função deve escrever no arquivo os dados da matriz m passada como segundo parâmetro.
# Cada linha do arquivo deve conter uma linha da matriz. Por último, a função fecha o arquivo e retorna a matriz m.

def salvamat(nomearq,m):
    arquivo_processado = open(f"{nomearq}" , "wt")
    for i in range(len(m)):
        arquivo_processado.write(str(m[i]) + '\n')
    arquivo_processado.close()
    print("Arquivo gerado")
    return m

# c) No mesmo programa python do item anterior, escreva a função somaMat(ma,mb).
# Esta função recebe como parâmetros de entrada 2 matrizes de ints.
# A função devolve uma terceira matriz contendo a soma das duas matrizes de entrada.
# Pesquise na internet a regra para a soma de matrizes.

def somaMat(ma,mb):
    if (len(ma) == len(mb)) and len(ma[0]) == len(mb[0]):
        linha = len(ma)
        coluna = len(mb[0])
        lst_out = []
        for i in range(linha):
            lst_aux = []
            for j in range(coluna):
                lst_aux.append(ma[i][j] + mb[i][j])
            lst_out.append(lst_aux)
        print(lst_out)
    return lst_out

# d) Construa uma função main que utiliza as funções em a), b) e c) para carregar, somar e
# salvar o resultado da soma das matrizes nos arquivos matA5x10.txt e matB5x10.txt.
# Esses dois arquivos são fornecidos como material da tarefa.
# O arquivo de saída deve ser nomeado soma5x10.txt.

def main():
    ma = loadmat(arquivoA)
    mb = loadmat(arquivoB)
    soma = somaMat(ma,mb)
    salvamat(arquivoSaida,soma)

if __name__ == '__main__':
    main()


