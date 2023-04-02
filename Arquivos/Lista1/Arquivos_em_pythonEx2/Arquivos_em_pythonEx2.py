# 2. Construa um programa python para fazer a concatenação de 2 arquivos textos em um terceiro arquivo texto de detino.
# Os nomes dos arquivos podem ser fornecidos pelo usuário ou definidos como constantes.
# Todos os arquivos devem ser processados linha a linha..
# Ao final do procesamento, o arquivo de saída deve possuir todo o conteúdo do primeiro arquivo seguido de todo o conteúdo do segundo arquivo.
# Veja o modelo exemplo a seguir:

# Arquivo A:              Arquivo B:                     Arquivo Saida:
# A1A1A1A1A1A1A1          B1B1B1B1B1B1                   A1A1A1A1A1A1A1
# A2A2A2A2A2A2A2          B2B2B2B2B2B2                   A2A2A2A2A2A2A2
# A3A3A3A3A3A3A3                                         A3A3A3A3A3A3A3
#                                                        B1B1B1B1B1B1
#                                                        B2B2B2B2B2B2

input_arq_a = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Arquivos\\Arquivos_em_pythonEx2\\Arquivo_A.txt"
input_arq_b = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Arquivos\\Arquivos_em_pythonEx2\\Arquivo_B.txt"
output_arq = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Arquivos\\Arquivos_em_pythonEx2\\Arquivo_Processado.txt"

##############

arquivo_A = open(f"{input_arq_a}","rt")
lista_elementos_A = []

for linha in arquivo_A:
    if linha[-1] == '\n':
        elemento = linha[:-1]
    else:
        elemento = linha
    lista_elementos_A.append(elemento)
arquivo_A.close()

##############

arquivo_B = open(f"{input_arq_b}","rt")
lista_elementos_B = []

for linha in arquivo_B:
    if linha[-1] == '\n':
        elemento = linha[:-1]
    else:
        elemento = linha
    lista_elementos_B.append(elemento)
arquivo_B.close()

###############

lista_elementos_C = lista_elementos_A + lista_elementos_B
print(lista_elementos_C)
###############

arquivo_processado = open(f"{output_arq}","wt")
for i in range(len(lista_elementos_C)):
    arquivo_processado.write(lista_elementos_C[i]+'\n')
arquivo_processado.close()
