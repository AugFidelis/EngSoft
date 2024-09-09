resp = str(input("Telefonou para a vítima? "))

positivos = 0

if(resp == 'S'):
    positivos += 1

resp = str(input("Esteve no local do crime? "))

if(resp == 'S'):
    positivos += 1

resp = str(input("Mora perto da vítima? "))

if(resp == 'S'):
    positivos += 1

resp = str(input("Devia para a vítima?" ))

if(resp == 'S'):
    positivos += 1

resp = str(input("Ja trabalhou com a vítima? "))

if(resp == 'S'):
    positivos += 1

if(positivos < 2):
    print("Inocente")
elif(positivos == 2):
    print("Suspeita")
elif(positivos > 2 and positivos != 5):
    print("Cumplice")
else:
    print("Assassino")


