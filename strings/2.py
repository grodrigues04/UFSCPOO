'''Verificar se uma frase (String) é palíndromo. A entrada é uma frase e a saída é um valor lógico (verdade ou falso) indicando se a frase é um palíndromo ou não.

Exemplo de entrada: 

a cara rajada da jararaca

Saída:

True'''

fraseOriginal = input() .replace (' ', '')
for letra in fraseOriginal:
    if letra.isalpha():
        pass
    else:
        fraseOriginal = fraseOriginal.replace(letra,'')

fraseTeste = fraseOriginal[::-1]

print(fraseTeste==fraseOriginal)