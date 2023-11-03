n = int(input())
sequencia = []
somatoria = 0
for c in range(n):
    num = float(input())
    sequencia.append(num)

ma = sum(sequencia)/len(sequencia)
valores = []

for numeros in sequencia:
    valores.append(((numeros-ma))**2)

desvio = (sum((valores/n-1)))**(1/2)


