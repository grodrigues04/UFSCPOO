#https://www.beecrowd.com.br/repository/UOJ_2552.html
while True:
    
    try:
        n,m = [int(x) for x in input().split()]
        matriz = []
        for j in range(n):
            matriz.append([int(x) for x in input().split()]) #criando a matriz
        for i in range(n):
            for j in range(m):
                if matriz[i][j]==1: #percorrendo a matriz e verificando se o elemento é 1
                    matriz[i][j]=9
        for l in range(n):
            for c in range(m):
                if matriz[l][c]==0:
                    adjacente = 0
                    for i,j in((l-1,c), (l+1,c), (l,c+1), (l,c-1)):
                        if i in range(n) and j in range(m) and matriz[i][j] == 9:
                            adjacente= adjacente + 1
                    matriz[l][c] = adjacente
        for linha in matriz:
            print(''.join([str(x) for x in linha]))
    except EOFError:
        break