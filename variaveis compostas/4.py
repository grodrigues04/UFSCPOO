lista1 = []
lista2 = []
ordem = []
n1 = int(input())
for c in range(n1):
    nomes = input()
    lista1.append(nomes)
n2 = int(input())
for c in range(n2):
    nomes = input()
    lista2.append(nomes)
menorLista = min(len(lista1),len(lista2))
while menorLista != 0:
    if lista1[0] < lista2[0]:
        ordem.append(lista1[0])
        lista1.pop(0)
    else:
        ordem.append(lista2[0])
        lista2.pop(0)
    menorLista = min(len(lista1),len(lista2))
if (len(lista1)) > (len(lista2)):
    for nome in lista1:
        ordem.append(nome)
else:
    for nome in lista2:
        ordem.append(nome)
for nome in ordem:
    print(nome)