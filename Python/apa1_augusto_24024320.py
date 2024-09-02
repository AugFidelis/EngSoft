###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 1 - Rumo a Marte
# Nome: Augusto Fidelis dos Santos Custódio
# RA: 24024320
###################################################

D1 = float(input())
V1 = float(input())
T = float(input())
D2 = float(input())
V2 = float(input())

T = T * 24

T1 = D1/V1
T2 = D2/V2 + T

if(T1 < T2):
    print("True")
else:
    print("False")