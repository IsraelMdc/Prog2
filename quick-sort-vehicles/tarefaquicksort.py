import modquicksort

#Método auxiliar para salvar os arquivos de saída.
def gera_arquivo_saida(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for elemento in lista:
            arquivo.write(f'{elemento["placa"]},{elemento["modelo"]},{elemento["marca"]},{elemento["quilometragem"]},{elemento["cor"]},{elemento["combustivel"]}\n')

def carregabd(nome_arquivo):
    
    with open(nome_arquivo, "r") as arquivo:

        #Lista que irá armanezar os veiculos
        veiculos = []

        #Percorre todas as linhas do arquivo.
        for linha in arquivo:

            #Criamos uma lista com as informações separadamente.
            informacoes = linha.rstrip("\n").split(",")

            #Criamos um objeto para armazenar as informações.
            veiculo = {
                "placa": informacoes[0], 
                "modelo": informacoes[1], 
                "marca": informacoes[2], 
                "quilometragem": informacoes[3], 
                "cor": informacoes[4], 
                "combustivel": informacoes[5]
                }

            veiculos.append(veiculo)

    return veiculos

# Chamando os métodos de ordenação e gera os arquivos de saída.
gera_arquivo_saida(modquicksort.quickr(carregabd("bdveiculos2.txt")), "quickr-out.txt")
gera_arquivo_saida(modquicksort.quickr(carregabd("bdveiculos2.txt")), "quicknr-out.txt")