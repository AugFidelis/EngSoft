# lista = []

# for i in range(10):
#     n = int(input())
#     lista.append(n)

# for i in range(9,-1,-1):
#     print(lista[i],end=" ")

#--------------------------------- Outro jeito de fazer:

lista = []

for i in range(10):
    n = int(input())
    lista.append(n)

lista_inversa = []

for i in range(10):
    x = lista.pop() #Apaga o último valor da lista e guarda no x
    lista_inversa.append(x) #Insere o valor na nova lista inversa

print(lista_inversa)

