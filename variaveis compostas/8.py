'''Dada uma frase, queremos saber qual a letra que mais aparece, trabalhando sempre com letras minúsculas, 
ou seja, desconsiderando a distinção dentre letras maiúsculas e minúsculas. O dado de entrada é uma frase e 
o resultado é a letra que mais ocorre, conforme exemplo abaixo.

Exemplo de entrada:

Hoje acordei com vontade de tomar sorvete  de cereja

Saída:

e'''

frase = input().lower().replace(' ', '')
repetiu = 0
letraR = str
for letra in frase:
    if frase.count(letra) > repetiu:
        repetiu = frase.count(letra)
        letraR = letra
print(letraR)
