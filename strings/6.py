'''Considere que Mariazinha tenha realizado uma prova de múltipla escolha. 
Desejamos, agora, determinar o número de acertos de Mariazinha. Para tal, 
são fornecidos o gabarito e as respostas em duas linhas consecutivas, ambos 
na forma de um String de mesmo comprimento. A entrada pode ser dada como abaixo, 
sendo o resultado um número inteiro correspondente ao número de acertos (5, neste caso)
Exemplo de entrada:
abcbdab
aecbaab

Saída:
5'''

gabarito = input()
resposta = input()
acertos = 0
for c in range(len(gabarito)):
    if gabarito[c]==resposta[c]:
        acertos+=1
print(acertos)
        