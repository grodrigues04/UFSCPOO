from math import log10 
'''log10 ajuda a calcular quantos digitos de dezena um número tem.
Assim, consigo determinar quantos zeros preciso colocar na frente dos numeros iniciais
 '''

linha_atual = 1
entrada= int(input())
total = 0
zero = "0"

while linha_atual < entrada:
    total = total+linha_atual
    linha_atual= linha_atual + 1

total = (total+entrada)

linha = 1
numero = 1
while linha_atual < entrada:
    total = total+linha_atual
    linha_atual=+1
while linha <= entrada:
    coluna = 0
    while coluna < linha:
        n_de_zero = int(log10(total)) - int(log10(numero))
        controle = 0
        ctrZero = ""
        while controle < n_de_zero:
            ctrZero = ctrZero + zero
            controle+=1
        printador = f'{ctrZero}{numero}'
        print(printador,end=' ')
        numero = numero+1
        coluna = coluna + 1
    linha = linha + 1
    print()
