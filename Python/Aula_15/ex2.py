'''
2) Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma
poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total
ganho com juros no período.
'''

deposito_ini = float(input('Insira o valor do depósito: '))
juros = float(input('Insira o valor da taxa de juros: '))

deposito = deposito_ini
juros /= 100
i = 1

while(i <= 24):
    print(f'Mês {i}: R${deposito :.2f}, com ganho total de R${deposito - deposito_ini :.2f} em juros')
    deposito += (deposito * juros)
    i += 1
