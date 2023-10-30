def clear():
    print('-'*70)

def miniclear():
    print('*'*30)
nome = 'ola joão'
#s[:sstarttop:step]
clear()#----------------------------------------------------------------------------------------------------


print('Nome de tras para frente')
print(nome[-1::-1])


clear()#----------------------------------------------------------------------------------------------------


#percorrer a string
print('Percorrendo a string')
for letra in nome:
    print(letra)

clear()
#for letra in nome[:-2]: #tirando as duas ultimas letras
 #   print(letra)
#----------------------------------------------------------------------------------------------------

#Verificar se uma palavra não está na string

if 'jose' not in nome:
    print('José não está na string')

if 'joão' in nome:
    print('João está na string!')
clear()#----------------------------------------------------------------------------------------------------
#Métodos da classe 'str'
s = "Olá, João Carlos"
type(s)
miniclear()#----------------------------------------------------------------------------------------------------------------
print(s.upper()) #Obter uma nova string que é cópia da anterior porém com todas as letras transformadas para maiúsculas

miniclear()#----------------------------------------------------------------------------------------------------------------

print(s.lower())#string em letras minusculas(a original ainda não foi alterada)

miniclear()#----------------------------------------------------------------------------------------------------------------

s.split()# Dividir uma string em pedaços (por padrão o critério de divisão é caracter em branco)
s.split(',')# Dividir uma string em pedaços, utilizando o caracter ',' como critério de divisão
print(s)

miniclear()#----------------------------------------------------------------------------------------------------------------

print(s.count('o'))#contar o numero de vezes que uma determina letra aparece
frase = "O carro atropelou o carcará"
print(frase.count('car'))

miniclear()#----------------------------------------------------------------------------------------------------------------
# Contar o número de ocorrências não sobrepostas de uma posição até outra
frase.count('car', 8, 24)

miniclear()#----------------------------------------------------------------------------------------------------------------
a= (frase.index('atr')) #pega o indice da primeira letra
print(frase[a::])

miniclear()#----------------------------------------------------------------------------------------------------------------

#split != strip 
#strip tira caracteres do INICIO e do FINAL. Por padrão, remove os espaços em branco, mas nunca do meio de uma string
a = 'ÇgustÇavoÇ'
print(a.strip('Ç')) #nota que o "Ç" do meio continou lá
miniclear()#----------------------------------------------------------------------------------------------------------------
# Substituir uma string por outra
frase.replace('car', 'ZZZ')

# Substituir uma string por string vazia (equivale a excluir)
frase.replace('car', '')
# Lembrar que é gerada uma nova string e que a original não é alterada (imutável)

miniclear()#----------------------------------------------------------------------------------------------------------------

# Verifica se todos os caracteres da string são dígitos numéricos 
str = "123456"
print(str.isdigit()) #retorna valor booleano

#verifica se todos os caracteres da string são letras
str = "Abracadabra"
print(str.isalpha()) 

# Verifica se todos os caracteres da string são dígitos numéricos ou letras

str = "Abc123"
print(str.isalnum()) 

#nota: Antonio e Antônio são diferentes, pois o valor decimal correspondendo ao caracter 'o' e 'ô' são diferentes. Isso ocorre para letras maiusculas e minuscula
print(ord('o'))
print(ord('^'))
print(ord('ô'))

#verificar quem vem antes em ordem lexicográfica(ordem alfabetica)
print("Maria das Dores" < "Maria do Rosário")
a = "Maria das Dores" 
for letra in a:
    letra = letra
    print(ord(letra))