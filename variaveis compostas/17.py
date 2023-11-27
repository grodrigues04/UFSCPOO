#https://www.beecrowd.com.br/repository/UOJ_2227.html
A,V= [int(x) for x in input().split()] #aeroportos, voos.
teste = 1
while A!= 0:
    frequencia = []
    dicionario = {}
    voos = []
    for c in range(V):
        voos.append(tuple([int(x) for x in input().split()]))
    for d in range(len(voos)):
        for x in range(2):
            frequencia.append(voos[d][x])
    for m in range(1,A+1):
        dicionario[m] = frequencia.count(m)
    trafegos = (max(dicionario.values()))
    chaves_mais_altas = [chave for chave, valor in dicionario.items() if valor == trafegos]
    print(f" Teste {teste}")
    print(*chaves_mais_altas,end=' ')
    print('')
    teste +=1
    A,V= [int(x) for x in input().split()]
   