def main():

    cont = 0
    total_fabrica = 0
    total_pecas = 0
    cont_a = 0
    cont_b = 0
    cont_c = 0
    cont_M = 0
    cont_F = 0
    cont_salario_total_classe_1 = 0
    cont_salario_total_classe_2 = 0
    cont_salario_total_classe_3 = 0
    cont_M_1 = 0
    cont_M_2 = 0
    cont_M_3 = 0
    cont_F_1 = 0
    cont_F_2 = 0
    cont_F_3 = 0

    nmr_maior_salario = None

    num_operario= int(input('NUMERO DO OPERARIO:'))
    while num_operario != 0:
        num_peças= int(input('NUMERO DE PEÇAS POR MES: '))
        sexo_operario= str(input('M OU F?'))
        cont = cont + 1
        salario_minimo = 1320
        
        if sexo_operario == 'F':
            cont_F += 1
        if sexo_operario == 'M':
            cont_M += 1

        if num_peças == 30:
                print(f'CLASSE A, RECEBE {salario_minimo}')
                cont_a += 1
                cont_salario_total_classe_1 += cont_salario_total_classe_1 
                if sexo_operario == 'M':
                    cont_M_1 += 1
                else:
                    cont_F_1 += 1 

        elif num_peças >= 31 and num_peças <= 35:
                salario_minimo = salario_minimo + (salario_minimo * 0.03 * (num_peças - 30 ))
                print(f'CLASSE B, RECEBE {salario_minimo}')
                cont_b += 1
                cont_salario_total_classe_2 += cont_salario_total_classe_2 
                if sexo_operario == 'M':
                    cont_M_2 += 1
                else:
                    cont_F_2 += 1 

        else:
            salario_minimo = salario_minimo + (salario_minimo * 0.05 * (num_peças - 30 ))
            print(f'CLASSE C, RECEBE {salario_minimo}')
            cont_c += 1
            cont_salario_total_classe_3 += cont_salario_total_classe_3 
            if sexo_operario == 'M':
                cont_M_3 += 1
            else:
                cont_F_3 += 1 


        if salario_minimo > nmr_maior_salario:
             nmr_maior_salario = num_operario


        total_fabrica += salario_minimo
        total_pecas += num_peças

        num_operario= int(input('NUMERO DO OPERARIO:'))  

    print(f"Total fábrica = {total_fabrica}")              
    print(f"Total fábrica = {total_pecas}")
    print(f"Total de peças fabricadas por homens: {total_fabrica/cont - cont_M}")
    print(f"Total de peças fabricadas por homens classe 1: {cont_salario_total_classe_1/cont_M_1}")
    print(f"Total de peças fabricadas por homens classe 2: {cont_salario_total_classe_2/cont_M_2}")
    print(f"Total de peças fabricadas por homens classe 3: {cont_salario_total_classe_3/cont_M_3}")
    
    print(f"Total de peças fabricadas por mulheres: {total_fabrica/cont - cont_F}")
    print(f"Total de peças fabricadas por mulheres classe 1: {cont_salario_total_classe_1/cont_F_1}")
    print(f"Total de peças fabricadas por mulheres classe 2: {cont_salario_total_classe_2/cont_F_2}")
    print(f"Total de peças fabricadas por mulheres classe 3: {cont_salario_total_classe_3/cont_F_3}")


    print(f"Numero do operador com maior salário: {nmr_maior_salario}")

if __name__ in '___main__':
    main()