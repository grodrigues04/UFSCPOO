'''Dada uma sequência de nomes (um em cada linha), contar quantos destes nomes contém 
como parte dele o nome "Maria". Nos dados de entrada, na primeira linha há um número 
inteiro indicando quantos nomes veem abaixo.

Exemplo de entrada:

3
Maria da Luz
João Pedro Nogueira
João Maria Lima

Saída:

2'''

n = int(input())
marias = 0
for c in range(n):
    nomes = input().lower()
    nomes_separados = nomes.split()
    if "maria" in nomes_separados:
        marias+=1
print(marias)
