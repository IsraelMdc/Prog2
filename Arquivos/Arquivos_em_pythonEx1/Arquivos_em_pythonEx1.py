# Arquivos_em_python

# 1. Construa um programa python para fazer a cópia de um arquivo texto para outro
# arquivo texto. Os nomes dos arquivos podem ser fornecidos pelo usuário ou definidos
# como constantes. O arquivo de entrada deve ser processado linha a linha. Ao final do
# procesamento, o arquivo de saída deve possuir um conteúdo idêntico ao arquivo de
# entrada.

lista = []
input = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Arquivos\\BaseTeste.txt"
output = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Arquivos\\BaseTesteProcessada.txt"


arquivo = open(f'{input}',"rt")

for linha in arquivo:
    if linha[-1] == '\n':
        elemento = linha[:-1]
    else:
        elemento = linha
    
    lista.append(elemento)

arquivo_saida = open(f'{output}',"wt")
for i in range(len(lista)):
    arquivo_saida.write(lista[i]+'\n')

arquivo_saida.close()
arquivo.close()
print(lista)