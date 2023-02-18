# Formas de entregar atributos de uma função

def salvar_carro(marca, modelo, ano, placa):
    
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')
    
salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234') # Mais comum (daria problema se alguem trocasse a ordem de algum argumento)

salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1234') # Daria problema se alguém não colocasse um dos argumentos

salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1234 '})
# * args = significa que vai receber uma tupla como argumento
# ** kwargs = significa que vai receber um dict como argumento
