def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
# A barra(/) fala que tudo que vier antes dela deve ser solicitado apenas por posição, e o que vier depois dela, por chave ou posição.

criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')