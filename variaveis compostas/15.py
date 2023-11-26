#https://www.beecrowd.com.br/repository/UOJ_2366.html
N, M = [int(x) for x in input().split()]
distancia = [int(x) for x in input().split()]
consegue = 'S'
for c in range(len(distancia)-1):
    if distancia[c+1]-distancia[c]>M:
        consegue = 'N'
        break
print(consegue)
        