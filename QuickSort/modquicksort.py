def ordena_pivo(lista, inicio, fim, aux):
    indice = inicio - 1
    pivo = lista[fim][aux]

    for j in range(inicio, fim):
        if lista[j][aux] <= pivo:
            indice = indice + 1
            lista[indice], lista[j] = lista[j], lista[indice]
    lista[indice + 1], lista[fim] = lista[fim], lista[indice + 1]

    return indice + 1

def quickr(lista, inicio, fim, aux):
    if inicio < fim:
        pi = ordena_pivo(lista, inicio, fim, aux)

        quickr(lista, inicio, pi - 1, aux)
        quickr(lista, pi + 1, fim, aux)


def quicknr(lista, aux):
    lst = []
    lst.append((0, len(lista) - 1))

    while lst:
        inicio, fim = lst[-1]

        if inicio < fim:
            pi = ordena_pivo(lista, inicio, fim, aux)


            lst = lst[:-1]

            lst.append((inicio, pi - 1))
            lst.append((pi + 1, fim))
        else:

            lst = lst[:-1]

    return lista


def quicksort(lista, aux):
    quickr(lista, 0, len(lista) - 1, aux)
    return lista