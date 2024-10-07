num = int(input("Insira o tamanho: "))

for i in range(1,num+1):
    for j in range(i-1):
        print("*",end=" ")

    print("+",end=" ")

    for k in range (i,num):
        print("*",end=" ")

    print()