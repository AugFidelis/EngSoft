maior = 0
for i in range(1,6):
    num = float(input(f"Insira o número {i}: "))
    if(num > maior):
        maior = num

print(f"O maior número é: {maior}")