lista = []
lista2 = []

while(True):
    item = input("Insira um valor para a lista (digite 'pare' para parar): ")

    if(item == 'pare'):
        break

    lista.append(item)

    while(True):
        opc = str(input("Deseja buscar um valor na lista? (Digite 'n' caso não): "))

        encontrado = False

        if(opc == 'n'):
            break
        else:
            pesquisa = input("Digite o valor a pesquisar: ")

            for i in range(len(lista)):
                if(pesquisa == lista[i]):
                    encontrado = True
                    indice = i
                    
                    lista2.append(lista[i])
                    del lista[i]
                    break

            if(encontrado == True):
                print(f"Elemento encontrado na posição {indice} da lista.")
            else:
                print("Elemento não está na lista.")

print(lista)
print(lista2)


