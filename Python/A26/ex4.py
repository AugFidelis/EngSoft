nome = str(input("Nome: "))


for i in range(len(nome)):
    for j in range(i+1):
        print(nome[j],end="")

    print()
