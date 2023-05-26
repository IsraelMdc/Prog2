hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
lst = []
lst_resposta = []
n = int(input())
v = 16

while n > 0:
    r = n%v
    n = n//v
    lst.append(r)
    print('entrada',lst)

lst.reverse()
print('revertida',lst)

for i in lst:
    s = hex[i]
    lst_resposta.append(s)
    print(s)
print(lst_resposta)