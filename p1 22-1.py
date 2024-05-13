from random import randint #so pra gerar uma lista aleatória e testar o algoritmo
#Resolução prova https://docs.google.com/document/d/1-Xam0HnnkvDpaJiJhE9ap6HYjCLAmW-oCTrPyfc9oX0/edit
#-----------------------------------------------------------------------------------------------------------
#Questão 1:
#-----------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------
#Questão 2:
#-----------------------------------------------------------------------------------------------------------
def indiceDoElemento(lista,numero): #função que resolve 2A
    controle = 0
    while controle < len(lista):
        if lista[controle]==numero:
            return controle
        controle+=1
    return -1  #se terminar o while, significa que não encontrou nenhum

def mostraQuantidades(lista):
    listaDeElementos = []
    listaDoIndiceRep = []
    Controle = 0
    while Controle < len(lista):
        if lista[Controle] not in listaDeElementos:
            listaDeElementos.append(lista[Controle])
            Controle+=1
            listaDoIndiceRep.append(1)
        else:
            posicao = indiceDoElemento(lista,lista[Controle])
            if posicao >= len(listaDoIndiceRep):
                posicao = len(listaDoIndiceRep) - 1
            listaDoIndiceRep[posicao] = listaDoIndiceRep[posicao] + 1
            Controle+=1
        
    Controle = 0
    while Controle < len(listaDeElementos):
        print(f'O elemento {listaDeElementos[Controle]} repete-se {listaDoIndiceRep[Controle]} vezes')
        Controle+=1

#Gerando uma lista aleatoria so para testar:
listaExemplo = []
tamanho = randint(4,10)
for c in range(tamanho):
    listaExemplo.append(randint(1,5))
print(f'Lista criada: {listaExemplo}')

mostraQuantidades(listaExemplo) # Função que resolve 2B
