# 1. Faça um Programa que peça dois números e imprima o maior deles. Se os dois números
# forem iguais, imprima que são iguais.

num1 = float(input("Insira o número 1: "))
num2 = float(input("Insira o número 2: "))

if(num1 > num2):
    print(f"{num1} é maior que {num2}")
elif(num1 < num2):
    print(f"{num2} é maior que {num1}")
else:
    print("Os números são iguais.")