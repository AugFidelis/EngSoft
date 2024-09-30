base = int(input("Insira o valor da base: "))
exp = int(input("Insira o valor do expoente: "))

pot = base
for i in range(1,exp):
    pot *= base

print(f"{base}^{exp} = {pot}")