'''Dada uma cadeia de caracteres (String), verificar se ela forma um número de CPF válido,
 retornando verdadeiro (true) ou falso (false) conforme o caso. O CPF pode estar num formato
   'nnn.nnn.nnn-nn' ou pode ser um número inteiro (sem ponto e hífen).

Além do formato, devem ser validados os dois dígitos verificadores do CPF.

Exemplo de entrada:
234.756.890-93
Saída:
False'''

cpf = input()
verificador = cpf[0]
total1 = 0
total2 = 0
cpf = ''.join(filter(str.isdigit, cpf))
if cpf.count(verificador)==11:
    print(False)
else:  
    for c in range(len(cpf)-2):
        total1 = (int(cpf[c])*(10-c) ) + total1
        total2 = (int(cpf[c])*(11-c) )+total2
    dv1 = 11 - (total1%11)
    total2 = dv1*2 + total2
    dv2 = 11 - (total2%11)

    if dv1>=10:
        dv1 = 0
    elif dv2>=10:
        dv2 = 0
    print(dv1==int(cpf[-2]) and dv2==int(cpf[-1]))

