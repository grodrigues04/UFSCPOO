'''No último trote solidário, os calouros do curso de Sistemas de Informação foram convidados a comparecer no Hospital Universitário para doar sangue.
A comissão organizadora do trote está interessada em saber se sua campanha foi bem sucedida. 
Para isto ela compilou duas listas de nomes, uma contendo os nomes dos calouros do curso e outra contendo os nomes de todas as pessoas 
que foram doar sangue no dia da campanha (esta última lista é geral, incluindo inclusive nomes de pessoas externas à universidade). O que
interessa à comissão é calcular a proporção de calouros que doaram sangue em relação ao total de calouros.

Nos dados de entrada, a primeira linha contém um valor inteiro correspondente ao número de calouros, seguida de outras linhas 
contendo os nomes desses calouros (um nome em cada linha). Em seguida vem outra linha contendo um valor inteiro que corresponde
à quantidade de doares (calouros ou não), seguida dos nomes dos doadores (um nome em cada linha).'''

#fazer a interscção da lista de doadores com a lista de calouros

calouros = set()
doadores = set()
interseccao = []
n = int(input())
for c in range(n):
    calouros.add(input())
n = int(input())
for c in range(n):
    doadores.add(input())

for doador in doadores:
    if doador in calouros:
        interseccao.append(doador)
print(len(interseccao))
print(len(doadores))
print(len(interseccao)/len(doadores))