def comparar(n1, n2):
    if(n1 > n2):
        print("Primeiro é maior")
    elif(n1 < n2):
        print("Segundo é maior")
    else:
        print("São iguais")

num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))

comparar(num1, num2)

num3 = float(input("Terceiro valor: "))
num4 = float(input("Quarto valor: "))

comparar(num3, num4)