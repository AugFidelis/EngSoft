def calculo_desconto(litros, tipo):
    if(tipo == 'A'):
        valor = litros * 2.90
        if(litros <= 20):
            valor = valor - (valor * 0.03)
        else:
            valor = valor - (valor * 0.05)

    elif(tipo == 'G'):
        valor = litros * 3.30
        if(litros <= 20):
            valor = valor - (valor * 0.04)
        else:
            valor = valor - (valor * 0.06)

    else:
        print('Tipo inválido')

    print(f'Valor a ser pago: R${valor}')

litros_comb = int(input('Quantos litros serão vendidos? '))
tipo_comb = str(input('Qual é o tipo de combustível? '))

calculo_desconto(litros_comb, tipo_comb)