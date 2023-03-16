# 1. Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. Após a
# leitura, percorra a lista original e aArmazene os números PARES em uma segunda
# lista e os números IMPARES em uma terceira lista. Ao final imprima as três listas.
qtdInteiros = 0
listaNumeros = []
listaPar = []
listaImpar = []

def inputDados(qtdInteiros,listaNumeros):
    while qtdInteiros < 20:
        pergunta = int(input("Digite um número inteiro: "))
        listaNumeros.append(pergunta)
        qtdInteiros = qtdInteiros + 1

    return listaNumeros

def separador(listaNumeros):    
    listaPar = []
    listaImpar = []
    for numero in range(len(listaNumeros)):
        if numero % 2 == 0:
            listaPar.append(numero)
        else:
            listaImpar.append(numero)
    return listaPar,listaImpar

inputDados(qtdInteiros,listaNumeros)
separador(listaNumeros)

print(listaNumeros)
print(f'Lista de números pares {listaPar}')
print(f'Lista de números Impares {listaImpar}')