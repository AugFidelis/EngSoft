maiores = 0
for i in range(20):
    num = float(input("Insira um número: "))
    if(num > 8):
        maiores += 1
    
print(f"Dentre os 20 números, {maiores} são maiores que 8.")