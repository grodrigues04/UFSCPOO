#https://www.beecrowd.com.br/repository/UOJ_1547.html
n = int(input())
for c in range(n):
    chutometro = 101
    qt,s = [int(x) for x in input().split()]
    alunos = [int(x) for x in input().split()]
    for chute in alunos:
        if chute==s:
            ganhador = alunos.index(chute)
            break
        elif abs(chute-s) < chutometro:
            chutometro = abs(chute-s)
            ganhador = alunos.index(chute)
    print(ganhador+1)