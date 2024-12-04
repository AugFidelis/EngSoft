n = int(input('Tamanho: '))
l1 = []
l2 = []

print('Primeira sequência: ')
valor = int(input())
l1.append(valor)
for i in range(n-1):
    valor = int(input())
    
    for j in range(len(l1)):
        if valor <= l1[j]:
            l1.insert(j, valor)
            # print(f'LISTA: {l1} INDICE: {j}')
            break

print('Segunda sequência: ')
valor = int(input())
l2.append(valor)
for i in range(n-1):
    valor = int(input())
    
    for j in range(len(l2)):
        if valor <= l2[j]:
            l2.insert(j, valor)
            # print(f'LISTA: {l2} INDICE: {j}')
            break

# resultado = l2
# for i in range(n):
#     for j in range(n):
#         if l1[i] <= l2[j]:
#             resultado.insert(j, l1[i])
#             break

print(f'Primeira: {l1}')
print(f'Segunda: {l2}')
# print(f'Resultado: {resultado}')

