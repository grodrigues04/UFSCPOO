entrada = int(input())
controle = 1
ast = entrada*2-1

while controle <= entrada:
    number	 = 0
    while number < controle:
        number = number + 1
        print(number,end='')
    astControle = 0
    while astControle < ast:
        print("*",end='')
        astControle = astControle + 1
    ast = ast - 2
    number = 0
    while number < controle:
        number = number + 1
        print(number,end='')
    print()
    controle = controle + 1
        
