def quickr(lista):
    #Caso lista esteja vazia ou com 1 elemento, logicamente, ela está ordenada
    if len(lista) <= 1:
        return lista
    else:
        #Primeiro elemento da lista passa a ser o pivô
        pivo = lista[0]

        #Criamos uma lista para armazenar o elementos menores que o pivô
        menores_que_o_pivo = []

        #Percorre lista a partir do elemento na posição 1 ([1:]). (Segundo elemento da lista)
        for elemento in lista[1:]:
            if compara_veiculos(elemento, pivo) <= 0:
                menores_que_o_pivo.append(elemento)

        #Ideia semelhante com o que foi feito anteriormente, só que agora verificamos os maiores que o pivô
        maiores_que_o_pivo = []
        for elemento in lista[1:]:
            if compara_veiculos(elemento, pivo) == 1:
                maiores_que_o_pivo.append(elemento)

        #Concatena as listas resultantes das chamadas recursivas
        return quickr(menores_que_o_pivo) + [pivo] + quickr(maiores_que_o_pivo)

def quicknr(lista):
    #Inicializamos um pilha onde cada elemento é um par de indices que delimita a faixa a ser ordenada
    pilha = [(0, len(lista) - 1)]

    #Executa enquanto a pilha não estiver vazia. (Verificar se len(pilha) < 0 está ok)
    while len(pilha) > 0:
        #Removemos o elemento da pilha e atribuímos os índices às suas respectivas variáveis
        menor_indice, maior_indice = pilha.pop()

        #Verificamos de modo a garantir que existem elementos a serem ordenados
        if menor_indice < maior_indice:
            indice_pivo = particao(lista, menor_indice, maior_indice)
            pilha.append((menor_indice, indice_pivo - 1))
            pilha.append((indice_pivo + 1, maior_indice))

    return lista

#Método auxiliar para o quicknr
def particao(lista, menor_indice, maior_indice):
    # Seleciona o pivô como o elemento no índice maior_indice
    pivo = lista[maior_indice]
    
    # Inicializa o índice i com menor_indice - 1
    i = menor_indice - 1
    
    # Percorre a faixa da posição menor_indice até maior_indice - 1
    for j in range(menor_indice, maior_indice):
        # Verifica se o elemento lista[j] é menor ou igual ao pivô

        if compara_veiculos(lista[j], pivo) <= 0:
            # Incrementa o índice i
            i += 1
            
            # Troca os elementos lista[i] e lista[j] de posição
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

    # Troca o pivô lista[maior_indice] com o elemento lista[i + 1]
    aux = lista[i + 1]
    lista[i + 1] = lista[maior_indice]
    lista[maior_indice] = aux
    
    # Retorna o índice i + 1, que representa a posição do pivô após a partição
    return i + 1

#Método auxiliar para comparar os veiculos
def compara_veiculos(veiculo1, veiculo2):

    # Comparar ordem alfabética crescente do combustível
    if veiculo1["combustivel"].lower() < veiculo2["combustivel"].lower():
        return -1
    elif veiculo1["combustivel"].lower() > veiculo2["combustivel"].lower():
        return 1

    # Comparar ordem alfabética crescente da cor
    if veiculo1["cor"].lower() < veiculo2["cor"].lower():
        return -1
    elif veiculo1["cor"].lower() > veiculo2["cor"].lower():
        return 1

    # Comparar ordem alfabética crescente da marca
    if veiculo1["marca"].lower() < veiculo2["marca"].lower():
        return -1
    elif veiculo1["marca"].lower() > veiculo2["marca"].lower():
        return 1

    # Comparar ordem decrescente do modelo
    if veiculo1["modelo"].lower() > veiculo2["modelo"].lower():
        return -1
    elif veiculo1["modelo"].lower() < veiculo2["modelo"].lower():
        return 1

    # Comparar ordem crescente da quilometragem
    if veiculo1["quilometragem"] < veiculo2["quilometragem"]:
        return -1
    elif veiculo1["quilometragem"] > veiculo2["quilometragem"]:
        return 1

    # Se todos os critérios forem iguais, retornar 0
    return 0