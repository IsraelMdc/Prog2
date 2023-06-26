hex = [" A","B","C","D","E","F"] #lista hex
numero = int(input("Digitae um numero; ")) #Numero qualquer
auxiliar = [] #auxiliar
while numero> 0: #10
    auxiliar.append(hex[(numero%16)]) #10 
    print(numero%16)
    print(auxiliar)
    numero=numero//16 #0 
    print(numero)
for i in range(len(auxiliar)-1,-1,-1): #0 
    print(auxiliar[i])
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,






























#AC10