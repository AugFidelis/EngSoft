n = int(input('Insira o tamanho dos vetores: '))
u = []
v = []

for i in range(n):
    valor = int(input())
    u.append(valor)

for i in range(n):
    valor = int(input())
    v.append(valor)

prodinterno = 0
for i in range(n):
    produto = u[i] * v[i]
    prodinterno += produto

print(prodinterno)
    