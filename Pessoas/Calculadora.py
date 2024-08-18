def main():    

    operador = menu()
    while operador != "sair":    
        if operador == "soma":
            resultado = soma()
        if operador == "subtracao":
            resultado = subtracao()
        if operador == "divisao":
            resultado = divisao()
        if operador == "multiplicacao":
            resultado = multiplicacao()
        if operador == "raiz quadrada":
            resultado = raiz_quadrada()
        if operador == "porcetagem":
            resultado = porcentagem()
        if operador == "potencia":
            resultado = potencia()    
        print(f"O resultado da operação escolhida foi de {resultado}.")
        operador = menu()
    
def menu():
    operador = str(input("\nDigite um dos operadores disponiveis sem acento para calcular ou digite sair para encerrar \n \n operadores disponíveis:\n\n soma \n multiplicacao \n divisao \n subtracao \n raiz quadrada \n porcentagem \n potencia \n\n "))
    return operador

def soma():
    valor1,valor2 = recebe_numero_normal()
    resultado = valor1 + valor2
    return resultado

def subtracao():
    valor1,valor2 = recebe_numero_normal()
    resultado = valor1 - valor2
    return resultado

def divisao():
    valor1,valor2 = recebe_numero_normal()
    resultado = valor1 / valor2
    return resultado

def multiplicacao():
    valor1,valor2 = recebe_numero_normal()
    resultado = valor1 * valor2
    return resultado

def potencia():
    valor1,valor2 = recebe_numero_normal()
    resultado = valor1 ** valor2
    return resultado

def raiz_quadrada():
    valor = int(input("Digite o valor a ser calculado: "))
    resultado = valor**(1/2)
    return resultado

def porcentagem():
    valor = int(input("Digite o valor a ser calculado: "))
    resultado = (valor * porcentagem)/100
    return resultado

def recebe_numero_normal():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    return valor1,valor2

main()