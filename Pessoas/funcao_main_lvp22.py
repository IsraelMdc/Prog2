import modulo_triangulo
def main():
    a = float()
    b = float()
    cont = 0
    area_triangulo = float()
    
    a = float(input('a-> '))
    b = float(input('b-> '))
    if a == 0 and b == 0:
        print(f'AREA={area_triangulo:.5f} A={a:.5f} B={b:.5f} ----------')
    else:
        while (cont == 0):
            if(a == 0 and b == 0):
                cont+=1
            else:
                if ((a == 0 and b == -1) or (a == -1 and b == 0)):
                    area_triangulo = modulo_triangulo.f_calcula_area_triangulo(a,b)
                    print(f'-----------AREA={(area_triangulo*-1):.5f} A={a:.5f} B={b:.5f}')
                    a = float(input('a-> '))
                    b = float(input('b-> '))
                else:
                    area_triangulo = modulo_triangulo.f_calcula_area_triangulo(a,b)
                    print(f'-----------AREA={area_triangulo:.5f} A={a:.5f} B={b:.5f}')
                    a = float(input('a-> '))
                    b = float(input('b-> '))

if __name__ in '__main__':
    main()

