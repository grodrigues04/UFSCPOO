competidores = dict()
carros, voltas = [int(x) for x in input().split()]
for c in range(carros):
    competidores[c] = sum([int(x) for x in input().split()])
ordem = dict(sorted(competidores.items(), key=lambda item: item[1]))
chaves = list(ordem.keys())
print((chaves[0])+1)
print((chaves[1])+1)
print((chaves[2])+1)
