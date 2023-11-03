valor = input().lower()
total = 0
c = 0
numeros = {"m":1000,"d":500,"c":100,"l":50,"x":10,"v":5,"i":1,"p":0
            }#p=0 resolve o problema de "string out of range"
valor = valor + 'p' 
while c < len(valor)-1:
    testes = valor
    if numeros[testes[c]] < numeros[testes[c+1]]:
        total = numeros[testes[c+1]] - numeros[testes[c]] + total
        c = c+2
    else:
        total = numeros[testes[c]] + total
        c = c+1
print(total)