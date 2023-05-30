valor_credito = 0
valor_debito = 0
cont = 0
maior_saldo = 0
menor_saldo = 0
clientes = int(input("digite o número de cliente:\n"))
for i in range(clientes):
    conta = input("Número da conta:\n")
    qtd_transacoes = int(input("Quantidade de transações:\n"))
    saldo_inicio_dia =float(input("Saldo da conta:\n"))
    for j in range(qtd_transacoes):
        tipo_transacao = input("Digite c para crédito e d para débito:\n")
        valor_transacao = float(input("Valor da transação:\n"))
        saldo_da_conta = saldo_inicio_dia
        if tipo_transacao == "c":
            valor_credito = valor_transacao + valor_credito
        if tipo_transacao == "d":
            valor_debito = valor_transacao + valor_debito
    valor_final = saldo_da_conta - valor_debito + valor_credito

    if valor_final < maior_saldo:
        maior_conta = conta
        maior_saldo = valor_final

    if valor_final < menor_saldo:
        menor_conta = conta
        menor_saldo = valor_final

    if valor_final <= 0:
        print(f"CONTA={conta} SALDO INICIAL={saldo_inicio_dia} SALDO FINAL={valor_final} SALDO INSUFICIENTE")
        cont = cont + 1
    else:
        print(f"CONTA={conta} SALDO INICIAL={saldo_inicio_dia} SALDO FINAL={valor_final}")
print(f'O MAIOR SALDO FINAL EH R${maior_saldo} NA CONTA {maior_conta}')
print(f'O MENOR SALDO FINAL EH R${menor_saldo} NA CONTA {menor_conta}')
print(f"{cont} CONTA(S) COM SALDO INSUFICIENTE")