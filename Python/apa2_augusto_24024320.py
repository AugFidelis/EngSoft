###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 2 - Ingresso de Cinema
# Nome: Augusto Fidélis dos Santos Custódio
# RA: 24024320
###################################################

dia_semana = int(input())
hora_inicio = int(input())
min_inicio = int(input())
estudante = str(input())
metodo_pag = str(input())

if((hora_inicio == 18 and min_inicio >= 30) or hora_inicio > 18):
    if(dia_semana == 1):
        ingresso = 30
        if(metodo_pag == 'C' and estudante != 'S'):
            ingresso = ingresso - (ingresso * 0.3)
        elif(estudante == 'S'):
            ingresso = ingresso - (ingresso * 0.5)

    elif(dia_semana == 2):
        ingresso = 20
        if(metodo_pag == 'C' and estudante != 'S'):
            ingresso = ingresso - (ingresso * 0.5)
        elif(estudante == 'S'):
            ingresso = ingresso - (ingresso * 0.5)

    elif(dia_semana == 3):
        ingresso = 30
        if(metodo_pag == 'C' and estudante != 'S'):
            ingresso = ingresso - (ingresso * 0.3)
        elif(estudante == 'S'):
            ingresso = ingresso - (ingresso * 0.5)

    elif(dia_semana == 4):
        ingresso = 30
        if(metodo_pag == 'C' and estudante != 'S'):
            ingresso = ingresso - (ingresso * 0.3)
        elif(estudante == 'S'):
            ingresso = ingresso - (ingresso * 0.5)

    elif(dia_semana == 5):
        ingresso = 30
        if(metodo_pag == 'C' and estudante != 'S'):
            ingresso = ingresso - (ingresso * 0.3)
        elif(estudante == 'S'):
            ingresso = ingresso - (ingresso * 0.5)

    elif(dia_semana == 6):
        ingresso = 30
        if(metodo_pag == 'C' and estudante != 'S'):
            ingresso = ingresso - (ingresso * 0.3)
        elif(estudante == 'S'):
            ingresso = ingresso - (ingresso * 0.5)

    elif(dia_semana == 7):
        ingresso = 30
        if(metodo_pag == 'C' and estudante != 'S'):
            ingresso = ingresso - (ingresso * 0.3)
        elif(estudante == 'S'):
            ingresso = ingresso - (ingresso * 0.5)

else:
    print("vespertino")