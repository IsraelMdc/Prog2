lst = [10,7,2,12,5,9]
cont = 1

while cont > 0:
    cont = 0 
    for i in range(len(lst)-1):
        if lst [i] > lst[i+1]:
            aux = lst[i]   
            lst[i] = lst[i+1]
            lst[i+1] = aux
            cont += 1
print(lst)
