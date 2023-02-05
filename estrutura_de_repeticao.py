# While

num = 0

while num < 10:
    num += 1
    print(num)
    
""" deposito = ['tomate', 'alface', 'cebola', 'vinagre', 'macarrao', 'feijao', 'couve', 'picanha']

def conferencia_deposito(item):
    for item in deposito:
        if item in deposito:
            print(f'{item}, OK \n')
    else:
        print('Não tem no depósito')
        
conferencia_deposito('arroz') """

""" FOR IN RANGE 

for numero in range(inicio, fim, step)
"""

#Tabuada de 5 com for range

for numero in range(0, 51, 5):
    print(numero, end =' ')
    print(' ')


# Condição infinita enquanto for verdade

""" while True:
    numero = int(input('Informe um número: '))
    
    if numero == 10:
        break
    
    #break serve para cortar a repetição
    
    print(numero) """
    
# Outra situação

for numero in range(101):
    if numero % 2 == 1:
        continue
    
# Continue ele vai pular e continuar executando
    
    print(numero, end=" ")