#https://www.beecrowd.com.br/repository/UOJ_1743.html

pluge = [int(x) for x in input().split()]
tomada = [int(x) for x in input().split()]
compat = 'Y'
for c in range(len(pluge)): #para este exercício, so precisamos achar 1 caso que seja falso para anular todo o resto.
    if pluge[c]==tomada[c]:#Quando esse caso for encontrado, break e print variiavel compt que reecebeu um N
        compat = 'N'
        break
print(compat)