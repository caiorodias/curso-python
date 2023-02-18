salario = 2000

def salario_bonus(bonus):
    global salario # Pra usar uma variável de fora da função é preciso avisar que é global.
    salario += bonus
    return salario

novo_salario = salario_bonus(500)

print(novo_salario)