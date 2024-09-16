'''
3. Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que
as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o
produto das idades do homem mais novo com a mulher mais velha.
'''

h1 = int(input('Idade do homem 1: '))
h2 = int(input('Idade do homem 2: '))
m1 = int(input('Idade da mulher 1: '))
m2 = int(input('Idade da mulher 2: '))

if(h1 > h2):
    if(m1 > m2):
        soma = h1 + m2
        produto = h2 * m1
    else:
        soma = h1 + m1
        produto = h2 * m2

else:
    if(m1 > m2):
        soma = h2 + m2
        produto = h1 * m1
    else:
        soma = h2 + m1
        produto = h1 * m2

print(f'A soma do homem mais velho e a mulher mais nova é: {soma}')
print(f'O produto do homem mais novo e a mulher mais velha é: {produto}')
