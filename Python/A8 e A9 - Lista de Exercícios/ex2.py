# 2. Faça um Programa que peça um valor diferente de zero e mostre na tela se o valor é
# positivo ou negativo. Se o número digitado for zero, imprima “Número inválido”.

valor = float(input("Insira um valor diferente de zero: "))

if(valor > 0):
    print("O valor é positivo.")
elif(valor < 0):
    print("O valor é negativo.")
else:
    print("Número inválido!")