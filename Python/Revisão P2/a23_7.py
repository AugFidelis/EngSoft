# 7. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo
# de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo
# desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de
# combustível. Calcule e mostre:
# a. O modelo do carro mais econômico;
# b. Quantos litros de combustível cada um dos carros cadastrados consome para
# percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando
# um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais
# próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
# programa.

carros = []
consumo = []

for i in range(5):
    print(f'Veiculo {i+1}')

    print('Nome: ',end='')
    carro = str(input())
    carros.append(carro)

    print('Km por litro: ',end='')
    cons = float(input())
    consumo.append(cons)

menorconsumo = 0
indice = 0
for i in range(5):
    if consumo[i] > menorconsumo:
        menorconsumo = consumo[i]
        indice = i

for i in range(5):
    print(f'{i+1} - ',end='')
    print(f'{carros[i]} - ',end='')
    print(f'{consumo[i]:.1f} - ',end='')
    
    quantlitros = 1000/consumo[i]
    print(f'{quantlitros:.2f} litros - ',end='')

    custo = quantlitros*2.25
    print(f'R$ {custo:.2f}')

print(f'O menor consumo é do {carros[indice]}')

