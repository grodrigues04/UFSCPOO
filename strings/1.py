'''Verificar dígito verificador de um número
Verificar se o dígito verificar (módulo 11) de um número dado na forma de um String está correto. 
Por exemplo, no número "14532", o dígito "2" é o dígito verificador do número. O resultado é verdade 
(true) ou falso (false) se o dígito verificador está correto ou não.
Considere que não é utilizado dígito verificado 'X'.

Exemplo de entrada:

14532

Saída:

True

'''

digito = input()
soma = 0
for c in range(len(digito)-1):
    soma = int(digito[c])*(len(digito) - c) + soma

digitoVerificador = 11-(soma%11)
print('digito verificador:', digitoVerificador)
if digitoVerificador >=10:   #cai fora das possiveis possibilidades
    digitoVerificador = 0

print(digitoVerificador== int(digito[-1]))