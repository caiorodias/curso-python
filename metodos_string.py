curso = '     Python    '

print(curso.upper())

print(curso.lower())

print(curso.title())

#tira os espaços da direita e esquerda
print(curso.strip())

#Tira os espaços da esquerda
print(curso .lstrip())

#Tira os espaços da direita
print(curso.rstrip())

curso2 = 'Python'

#coloca o caracter escolhido até que chegue na quantidade de caracter desejada
print(curso2.center(10,'#'))

print('.'.join(curso2))

# Formatar strings com f-string

pi = 3.14159

#print(f'Valor de PI: {pi:tamanho.casas apos virgulaf}')

print(f'Valor de PI: {pi:.2f}')

print(f'Valor de PI: {pi:10.2f}')

# Fatiamento de String

nome = 'Caio Rodrigo Dias da Silva'

print(nome[0])
# Primeira letra

print(nome[-1])
# Última letra

print(nome[:4])
# Do inicio ao 4 caractere

print(nome[13:])
# Do 13º caractere ao último

print(nome[13:17])
#do 13º ao 17º

print(nome[13:17:2])
# Do 13º ao 17º pulando 2 casas

print(nome[:: -1])
# Espelhar

# Strings triplas

name = 'Caio'

mensagem = f'''
    Olá, meu nome é {name},
Eu estou aprendendo Python.
        Essa mensagem tem diferentes recuos.
'''

# Com 3 aspas''' a string mantém os recuos.

print('''
      ============= Menu ============
      
      1 - Depositar
      2 - Sacar
      0 - Sair
      
      ================================
      
        Obrigado por usar nosso sistema!
'''
      )