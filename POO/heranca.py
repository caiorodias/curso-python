class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5
    
    def acelerar(self):
        print('Acelerando...')
        
    def frear(self):
        print('Freando...')
        
    def buzinar(self):
        print('Buzinando...')
        

carro = Carro()

carro.acelerar()


class Uno(Carro):   # herdeira(principal)
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992

uno = Uno()

print(uno.numero_rodas)  # Herdou tudo que tinha em Carro e acrescentou oq chegou em Uno

print(uno.marca)