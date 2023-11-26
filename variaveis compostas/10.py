#https://www.beecrowd.com.br/repository/UOJ_2189.html
#obs: o moodle e seus casos de teste é um lixo
num_ingressos = int(input())
teste = 0
testes = []
while num_ingressos!= 0:
    ingressos = [int(x) for x in input().split()]
    for index,value in enumerate(ingressos):
        if index==value-1:
            teste +=1
            testes.append(f'Teste {teste}')
            testes.append(value)
    num_ingressos = int(input())
print(testes)

