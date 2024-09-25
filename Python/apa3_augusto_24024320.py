###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 3 - Controle de Estoque
# Nome: Augusto Fidélis dos Santos Custódio
# RA: 24024320
###################################################

entrada = int(input())
estoque = 0
vendas = 0

while(entrada != 0):
    if(entrada > 0): #RE-ESTOQUE
        estoque += entrada
    else: #VENDA
        entrada = -entrada
        if(entrada > estoque):
            print(f"Quantidade indisponível para a venda de {entrada} unidades.")
        else:
            estoque -= entrada
            vendas += 1
    
    entrada = int(input())

print(f"Quantidade de vendas realizadas: {vendas}")
print(f"Quantidade em estoque: {estoque}")