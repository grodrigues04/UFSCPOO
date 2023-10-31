'''Dadas duas palavras, verificar se uma palavra é anagrama da outra.

Definição: "anagrama é uma palavra formada pela transposição das letras de outra".

Exemplo de entrada: 

capa
paca

Saída:True
'''

palavra1 = input()
palavra2 = input()
iguais = 0
if len(palavra1) != len(palavra2):
    print(False)
else:
    for letra1 in palavra1:
        iguais = palavra1.count(letra1) + iguais

print(iguais==len(palavra1))

