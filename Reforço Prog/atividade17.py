caminho = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Reforço Prog\\dadosEntrada.txt"
caminho_saida = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Reforço Prog\\dadosEntrada_processados.txt"

lista = []
arquivo= open(caminho,"rt")

for idade in arquivo:
    print (idade)
    idade = idade.rstrip('\n') 
    idade = int(idade)
    lista.append(idade)
lista.sort()
print (lista)

for i in range(len(lista)):
    print(lista[i])

arquivo_processado = open(f"{caminho_saida}","wt")
for i in range(len(lista)):
    arquivo_processado.write(str(lista)+ '\n')
arquivo_processado.close()





