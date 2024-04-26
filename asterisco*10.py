entrada = int(input())
controle = 1
ast = entrada*2-1
number = 1
controlNumber = 1
while controle <= entrada:
    print(number,end='')
    lastNumber = number
    controlNumber = controlNumber + 1
    number = number*10 + controlNumber
    astControle = 0
    while astControle < ast:
        print("*",end='')
        astControle = astControle + 1
    ast = ast - 2
    print(lastNumber,end='')
    print()
    controle = controle + 1
