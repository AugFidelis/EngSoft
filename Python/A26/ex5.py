calendario = str(input("Insira a sua data de nascimento (XX/XX/XXXX): "))
data = calendario.split('/')

print(f"Você nasceu em {data[0]} de {data[1]} de {data[2]}")