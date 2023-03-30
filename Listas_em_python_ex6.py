# 6. Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
# mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

listaTemperaturas = []

for mes in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média do mês{mes}"))
    listaTemperaturas.append(temperatura)

media_anual = sum(listaTemperaturas)/len(listaTemperaturas)

listaTemperaturasAcimaMedia = []

for mes,temperatura in enumerate(listaTemperaturas):
    if temperatura > media_anual:
        listaTemperaturasAcimaMedia.append((mes + 1, temperatura))

print(f"Temperaturas acima da média anual ({media_anual:.2f}):")

for mes,temperatura in listaTemperaturasAcimaMedia:
    nome_mes = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto', 'Setembro', 'Outubro','Novembro','Dezembro'][mes-1]
print(f"{nome_mes}: {temperatura:.2f}")