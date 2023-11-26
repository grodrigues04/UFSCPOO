''''Saque de valor em Caixa Eletrônico
Número máximo de arquivos: 2
Tipo de trabalho: Trabalho individual
Num caixa eletrônico estão disponíveis uma certa quantidade de cédulas de diferentes valores
e em ordem crescente de valor, conforme exemplificado abaixo. Quando um cliente realiza um saque,
é necessário determinar quantas cédulas de cada tipo serão necessárias para efetuar o saque.
Por exemplo, suponha que num caixa eletrônico tenhamos notas conforme a tabela abaixo:

Valor das cédulas	R$ 10.00	R$ 20.00	R$ 50.00	R$ 100.00
Quantidade de cédulas	50	20	20	10
Considerando que o critério para cálculo é o de oferecer ao cliente o menor número possível 
de notas, a título de exemplo considere que um cliente deseja realizar saque de  R$ 360,00. 
Neste caso são necessárias 3 notas de R$ 100,00, 1 nota de R$ 50,00 e 1 cédula de R$ 10,00.
 Note que é necessário também considerar o limite (quantidade) existente de cada cédula disponível 
 no caixa eletrônico.

Considere que sempre é possível obter o resultado, ou seja, que sempre há possibilidade de realizar o saque.

Para o exemplo acima, os dados de entrada então no formato indicado abaixo, sendo que o primeiro 
valor corresponde ao número de diferentes valores de cédulas disponíveis no caixa eletrônico, 
enquanto que o último corresponde ao valor do saque:

4
10.00
50
20.00
20
50.00
20
100.00
10
360.00


e a saída é:

1 0 1 3

'''
notas = dict()
n = int(input())
for _ in range(n):
    valor = float(input())
    qtd = int(input())
    notas[valor] = qtd
saque = float(input())

notas_necessarias = []
for valor in sorted(notas.keys(), reverse=True):
    qtd = min(int(saque / valor), notas[valor])
    saque -= qtd * valor
    notas_necessarias.append(qtd)

print(*notas_necessarias[::-1])




