#LISTAS ----------------------------------------------------------------------------------------------------------
lista = []

#[nome].append() adiciona algo ao final da lista:
lista.append(1)



#[nome].insert([indice],[valor]) adiciona algo na posição indicada pelo indice:
lista = [1, 2, 3, 4, 5]

lista.insert(3,420)

#RESULTADO: [1, 2, 3, 420, 4, 5]



#del nome[posicao] remove o que estiver na posição indicada:
del lista[0]

#RESULTADO: removeu o 1 no indice 0 -> [2, 3, 420, 4, 5]



#nome.remove(valor) remove o primeiro valor da lista que tenha o valor especificado:
lista.remove(4)

#RESULTADO: [2, 3, 420, 5]



#nome.pop() remove o ultimo item da lista
#pode ser atribuido a uma variável para salvar o valor removido:
removido = lista.pop()

#RESULTADO: [2, 3, 420]
#print(removido) = 5



#LISTAS II ----------------------------------------------------------------------------------------------------------

#Slicing cria uma sublista dos elementos contidos entre os índices especificados:

lista = [1, 2, 3, 4, 5, 6]
sublista = lista[1:3] #sublista = [2, 3, 4]

print(lista[1:3]) #RESULTADO = [2, 3, 4]



#Concatenação soma duas listas e gera uma nova lista que é as duas juntas

lista2 = [9, 8, 7, 1]

concat = lista + lista2

#RESULTADO: [1, 2, 3, 4, 5, 6, 9, 8, 7, 1]



#STRINGS ----------------------------------------------------------------------------------------------------------

#Strings são listas imutáveis:

string = 'Bom dia'

for i in range(3):
    print(string[i], end='') #RESULTADO = 'Bom'

for i in range(4,7):
    print(string[i], end='') #RESULTADO = 'dia'



#len(nome) retorna o tamanho da string, igual listas:

len(string) #RESULTADO: 7



#Concatenação funciona igual a lista:

string2 = 'Boa noite'

concat = string + string2 #RESULTADO: 'Bom diaBoa noite'

concat = string + ' e ' + string2 #RESULTADO: 'Bom dia e Boa noite'

print(string2 * 3) #RESULTADO: 'Boa noiteBoa noiteBoa noite'



#UPPER e LOWER convertem para maiúscula ou minúscula:

string2.upper() #RESULTADO: 'BOA NOITE'

string2.lower() #RESULTADO: 'boa noite'



#FUNÇÕES ----------------------------------------------------------------------------------------------------------

#Criar função:
def função(parametro1, parametro2):
    resultado = parametro1 + parametro2

    return resultado

#Chamar função:
x1 = 1
x2 = 5
res = função(x1,x2) #RESULTADO: res = 6