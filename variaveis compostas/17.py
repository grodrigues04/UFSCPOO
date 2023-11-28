#https://www.beecrowd.com.br/repository/UOJ_2227.html
num_aeroportos,num_voos= [int(user_input) for user_input in input().split()] #aeroportos, voos.
teste = 1
while num_aeroportos!= 0:
    lista_de_frequencia_total = []
    frequencia_do_aeroporto = {}
    voos = []
    for _ in range(num_voos):
        voos.append(tuple([int(x) for x in input().split()]))
    for vôo in range(len(voos)):
        for duplas in range(2):
            lista_de_frequencia_total.append(voos[vôo][duplas])
    for aeroporto in range(num_aeroportos):
        frequencia_do_aeroporto[aeroporto] = lista_de_frequencia_total.count(aeroporto)
    trafegos = (max(frequencia_do_aeroporto.values()))
    chaves_mais_altas = [chave for chave, valor in frequencia_do_aeroporto.items() if valor == trafegos]
    print(f" Teste {teste}")
    print(*chaves_mais_altas,end=' ')
    print('')
    teste +=1
    num_aeroportos,num_voos= [int(x) for x in input().split()]
   
