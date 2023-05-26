hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
n = int(input())
r = []

while n >0:
    r.append(hex[(n%16)])
    n = n//16

for i in range(len(r)-1,-1,-1):
    print(r[i], end= '')