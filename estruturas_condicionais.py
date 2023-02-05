import sys


opcao = int(input('Informe uma opção: [1] Sacar \n[2] Extrato: '))

saldo = 1000

if opcao == 1:
    valor = float(input('Informe a quantia para o saque: '))
    if valor > saldo:
        print('Saldo insuficiente')
    else:
        saldo -= valor
        print('Saque realizado, retire na boca do caixa!')
        print(f'Seu saldo atual é de R$ {saldo}')
elif opcao == 2:
    print('Exibindo o extrato...')
else:
    sys.exit('Opção inválida')