# Função dentro da função
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * 2 + b * 3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) #No função pode ser qualquer nome
    print(f'O resultado da operação {a} + {b} = {resultado}')
    
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, test)
    