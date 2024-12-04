A = int(input())
B = int(input())
C = int(input())

if(A == B and B == C):
    print("Não houve ganhador")
elif(B == C):
    print("Alice")
elif(A == C):
    print("Beto")
elif(A == B):
    print("Clara")

#-----------------------------------------------------------------------------------------------------------------------
'''
S = int(input())
O = int(input())
anos = 0

if(S < O):
    print("Orquídea já é maior.")

while(S >= O):
    S += 4
    O += 6
    anos += 1

if(anos > 0):
    print(f"O número de anos necessários para que a orquídea seja mais alta que a samambaia é: {anos} anos.")
'''

#-----------------------------------------------------------------------------------------------------------------------
''' 
niv0 = 0
niv1 = 0
niv2 = 0
num = 0
soma = 0

tempo = int(input())

tmax = tempo
tmin = tempo

while(tempo != -1):
    
    num += 1
    soma += tempo

    if(tempo <= tmax):
        tmax = tempo/60
        vmax = 33/tmax
    if(tempo >= tmin):
        tmin = tempo/60
        vmin  = 33/tmin

    if(tempo < 180):
        niv0 += 1
    elif(tempo < 240):
        niv1 += 1
    else:
        niv2 += 1

    tempo = int(input())

tempo_medio = soma/num

print(f"Caracois no nivel 0: {niv0}")
print(f"Caracois no nivel 1: {niv1}")
print(f"Caracois no nivel 2: {niv2}")

print(f"Tempo medio: {tempo_medio:.1f} s")

print(f"Velocidade maxima: {vmax:.1f} cm/min")
print(f"Velocidade minima: {vmin:.1f} cm/min")
'''

#-----------------------------------------------------------------------------------------------------------------------

'''
n = int(input())
linha = int(input())
coluna = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i == linha or j == coluna):
            print("x",end="")
        else:
            print("-",end="")

    print()

    input = x if x == 2 else 9 if y == 3 else 10 if z ==

    print("x" for i in range(10))

    var = 1 + 1 == 2 ? print(true) : print(false)

tabuleiro = [[("-" if x != POS[1] and y != POS[2] else "x") for x in range(1, SIZE+1)] for y in range(1, SIZE+1)]
'''

#-----------------------------------------------------------------------------------------------------------------------

'''
n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")

    print()

for i in range(1,n+1)
    for k in range(n-i):
        print(" ",end="")

    for j in range(i,0,-1):
        print(j,end="")

    print()
'''