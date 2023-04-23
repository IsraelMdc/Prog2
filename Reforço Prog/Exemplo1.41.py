comodo = str
classe = str
altura = float
comprimento = float
lampada = 60

while True:
    comodo = input()
    
    #Pontencia de iluminacao do comodo
    if comodo == "vazio":
        break

    classe = input()
    comprimento = float(input())
    largura = float(input())
    
    area = comprimento*largura
    if classe == "1":
        potencia = 15*area
    else:
        if classe == "2":
            potencia = area * 18
        else: 
            potencia = area * 20

    #lampadas do comodo
    lampadas = int(potencia / lampada)
    aux = float(potencia/lampada)

    if aux != lampadas:
        lampadas = lampadas + 1
    
    #total de lampadas da residencia
    total_lampadas = total_lampadas + lampadas

    #total de potencia da residencia
    total_potencia = total_potencia + potencia

    print(f'Cômodo da casa: {comodo}\n Área do cômodo: {area}\n Potencia do quarto: {potencia}\n Lâmpadas do cômodo: {lampadas}')

print(f"O total de lâmpadas da residencia é de: {total_lampadas} lamapadas\n O total da potencia da residência é de {total_potencia}")

    



