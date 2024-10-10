###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 4 - Jornada de Trabalho
# Nome: Augusto Fidélis dos Santos Custódio
# RA: 24024320
###################################################

V = int(input())
D = int(input())

tempo_total = 0
hora_extra = 0

for i in range(D):
    tempo_dia = 0
    num_periodos = int(input())
    
    for j in range(num_periodos):
        inicio = int(input())
        fim = int(input())
        
        for k in range(inicio, fim):
            
            tempo_dia += 1

            if(tempo_dia > 8):
                hora_extra += 1

            tempo_total += 1
            
if(tempo_total - hora_extra > 44):
    hora_extra = hora_extra + (tempo_total - hora_extra) - 44

valor_total = (V * tempo_total) + (V/2 * hora_extra)

print(f"Horas trabalhadas: {tempo_total}")
print(f"Horas extras: {hora_extra}")
print(f"Valor devido: R$ {valor_total :.2f}")