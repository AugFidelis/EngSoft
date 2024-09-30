soma = 0
for i in range(1,6):
    num = float(input(f"Insira o número {i}: "))
    soma += num

media = soma/5
print(f"A média é igual a {media}")