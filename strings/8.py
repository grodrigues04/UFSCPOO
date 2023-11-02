#https://www.beecrowd.com.br/repository/UOJ_1329.html link do enunciado


jogadas = int(input())
while jogadas != 0:
    resultado = input()
    maria = resultado.count('0')
    john = resultado.count('1')
    print(f'Mary won {maria} times and John won {john} times')
    jogadas = int(input())