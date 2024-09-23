'''
1) Escreva um programa de computador que peça para o usuário entrar com um
número inteiro n e que mostre como saída/resultado a tabuada para esse número.
Entretanto, o usuário também deve informar o início e fim da tabuada, ao invés de
começar obrigatoriamente com 0 e terminar com 10.
'''

num = int(input("Insira o número a ser multiplicado: "))
num_tab = int(input("Insira o número de início da tabuada: "))
fim = int(input("Insira o número do fim da tabuada: "))

while(num_tab <= fim):
    print(f"{num} X {num_tab} = {num * num_tab}")
    num_tab += 1

print("Fim")