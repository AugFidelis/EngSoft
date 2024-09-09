'''
6. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
de centenas, dezenas e unidades do mesmo.
Observe os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
1, 7 e 16
'''

num = int(input("Insira um número: "))

centenas = num // 100
dezenas = (num % 100) // 10
unidades = (num % 100 % 10) // 1

if(centenas == 0):
    if(dezenas == 0):
        print(f"{num} = {unidades} unidades")
    elif(unidades == 0):
        print(f"{num} = {dezenas} dezenas")
    else:
        print(f"{num} = {dezenas} dezenas e {unidades} unidades")

elif(dezenas == 0):
    if(centenas == 0):
        print(f"{num} = {unidades} unidades")
    elif(unidades == 0):
        print(f"{num} = {centenas} centenas")
    else:
        print(f"{num} = {centenas} centenas e {unidades} unidades")

elif(unidades == 0):
    if(centenas == 0):
        print(f"{num} = {dezenas} dezenas")
    elif(dezenas == 0):
        print(f"{num} = {centenas} centenas")
    else:
        print(f"{num} = {centenas} centenas e {dezenas} dezenas")

else:
    print(f"{num} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades")