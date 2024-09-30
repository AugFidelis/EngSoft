par = 0
impar = 0
for i in range(10):
    num = int(input("Insira um número: "))
    if(num%2 == 0):
        par += 1
    else:
        impar += 1

print(f"Pares: {par} / Ímpares: {impar}")