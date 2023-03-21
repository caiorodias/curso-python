class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    camera = False
    bateria = 'infinita'
    
    # Qualquer função dentro de uma class tem que ter o primeiro parâmetro self (que é uma instância da própria class)
    
    def fazer_ligacoes(self):
        print('Fazendo ligação...')
        
    def jogar_cobrinha(self):
        print('Jogando cobrinha...')
        
    def despertador(self):
        print('Despertando...')
        
    def calcular(self, v1, v2):
        return v1 + v2

celular = Celular()

print(celular.marca)

celular.fazer_ligacoes()

calculado = celular.calcular(3, 5)
print(calculado)