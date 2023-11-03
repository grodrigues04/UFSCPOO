nomeCompleto = input().split()
if len(nomeCompleto)<3:
    print(" ".join(nomeCompleto))
else:
    abreviado = []
    abreviado.append(nomeCompleto[0])
    for c in range(1,len(nomeCompleto)-1):
        if len(nomeCompleto[c])>3:
            abreviado.append(nomeCompleto[c][0] + ".")
        else:
            abreviado.append(nomeCompleto[c])

abreviado.append(nomeCompleto[-1])
print(" ".join(abreviado))