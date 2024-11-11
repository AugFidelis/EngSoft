lista = []
n = int(input("Tamanho da lista: "))

for i in range(n):
    print(f"Item {i+1}: ",end="")
    item = int(input())

    lista.append(item)

tamanho = int(input("Insira o tamanho do segmento: "))
soma = 0
indice = 0
soma_max = 0

for i in range(n):
    for j in range(i,i+tamanho):
        soma += lista[j]

    if(soma > soma_max):
        soma_max = soma
        indice_max = indice
        
    indice += 1

    soma = 0

print(f"Tamanho do segmento: {tamanho}")
print(f"Na sequência {lista}, a soma do segmento é {soma_max}")
print(f"Indice: {indice_max}")




