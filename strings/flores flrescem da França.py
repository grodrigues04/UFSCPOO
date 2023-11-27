fraseor = input()
frase = fraseor.lower().split()
while fraseor != '*':
    testador = frase[0][0]
    eh_tautograma = 'Y'
    for palavra in frase:
        if palavra[0]!=testador:
            eh_tautograma = 'N'
            break
    print(eh_tautograma)
    fraseor = input()
    frase = fraseor.lower().split()
    


