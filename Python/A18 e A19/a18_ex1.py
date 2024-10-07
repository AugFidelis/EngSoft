num = int(input("Insira um número inteiro: "))

opc = str(input("Escolha entre +, -, /, * ou 's' para sair: "))

while(opc != 's'):

    if(opc == '+'):
        for i in range(11):
            print(f"{num} + {i} = {num+i}")
    elif(opc == '-'):
        for i in range(11):
            print(f"{num} - {i} = {num-i}")
    elif(opc == '/'):
        for i in range(11):
            if(i == 0):
                print(f"{num} / {i} = 0")
            else:
                print(f"{num} / {i} = {num/i}")
    elif(opc == '*'):
        for i in range(11):
            print(f"{num} * {i} = {num*i}")

    opc = str(input("Escolha entre +, -, /, * ou 's' para sair: "))