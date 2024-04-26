entrada = int(input())
total = entrada*2-1
espaço = entrada - 1
numero = 1
controle_los = 1

def mostraespaço(n):
    controle = 0
    while controle <n:
        print(' ',end='')
        controle = controle + 1
        
while controle_los <= total:
    numero = 1
    mostraespaço(espaço)
    while numero <= controle_los:
        print(numero,end='')
        numero=numero + 1
    controle_los = controle_los + 2
    print()
    espaço = espaço -1

controle_los = controle_los -2
espaço = 1
while controle_los >= 0:
    numero = 1
    mostraespaço(espaço)
    controle_los = controle_los - 2
    while numero <= controle_los:
        print(numero,end='')
        numero=numero + 1
    print()
    espaço = espaço +1
