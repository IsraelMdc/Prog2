
#Diretório Absoluto de onde o arquivo de Origem(dados a serem processados) está
caminho = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Reforço Prog\\dadosEntrada.txt"
#Diretório Absoluto de onde o arquivo de Saída estará. 
#Obs: o arquivo será salvado com o último nome escrito no diretório e precisa ser diferente para que não sobrescreva arquivos
caminho_saida = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Reforço Prog\\dadosEntrada_processados.txt"

lista = []
#Abre o arquivo
arquivo= open(caminho,"rt")

#Extrai as idades do arquivo de origem
for idade in arquivo:
    print (idade)
    idade = idade.rstrip('\n') 
    idade = int(idade)
    lista.append(idade)
lista.sort()
print (lista)


#Mostra no console cada elemento na lista, um embaixo do outro
for i in range(len(lista)):
    print(lista[i])


#Função que cria e armazena os dados da lista em um novo arquivo usando o \n em cada linha
arquivo_processado = open(f"{caminho_saida}","wt")
for i in range(len(lista)):
    arquivo_processado.write(str(lista)+ '\n')
arquivo_processado.close()





