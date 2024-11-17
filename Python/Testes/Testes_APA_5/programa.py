###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 5 - Torre de Panquecas
# Nome: Augusto Fidélis dos Santos Custódio
# RA: 24024320
###################################################

torre = [int(panqueca) for panqueca in input().split()]

while True:
    M = int(input())

    if M == 0:
        break
    
    estavel = True
    inversa = []
    for i in range(M-1,-1,-1):
        inversa.append(torre[i])

    for i in range(len(inversa)):
        torre[i] = inversa[i]

    for i in range(1,len(torre)):
        if(torre[i-1] > torre[i]):
            estavel = False

if(estavel):
    print('Torre estavel')
else:
    print('Torre instavel')