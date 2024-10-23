#EX1 -------------------------------------------------

# n = int(input("Numero de vezes: "))

# f1 = 1
# f2 = 1

# print(f1,end=",")
# print(f1,end=",")

# for i in range(n):
#         x = f1+f2
#         f1 = f2
#         f2 = x
#         print(f2,end=",")

#EX2 ---------------------------------------

# f1 = 1
# f2 = 1

# print(f1,end=",")
# print(f1,end=",")

# while(f2 <= 500):
#         x = f1+f2
#         f1 = f2
#         f2 = x
#         print(f2,end=",")

#EX3 ---------------------------------------

# num = int(input("Numero fatorial: "))

# fat = 1

# print(f"{num}! = ",end="")
# for i in range(num,0,-1):
#     fat *= i
#     if(i != 1):
#         print(f"{i}*",end="")
#     else:
#         print(i,end="")

# print(f" = {fat}")

#EX4 ---------------------------------------

# n = int(input("Quant de numeros: "))

# num = int(input("Digite um número: "))

# maior = num
# menor = num
# soma = num

# for i in range(n-1):
#     num = int(input(f"Digite outro número: "))

#     if(num > maior):
#         maior = num
#     if(num < menor):
#         menor = num
    
#     soma += num

# print(f"O maior num é {maior}, o menor é {menor} e a soma é igual a {soma}")

#EX9 ---------------------------------------

# n = int(input("Quantidade: "))

# for i in range(2,n+1):
#     primo = True
#     divisor = 2

#     while divisor < i:
#         if(i % divisor == 0):
#             primo = False
#         divisor += 1

#     if(primo == True):
#         print(i,end=" ")
    







