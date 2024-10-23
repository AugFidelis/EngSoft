# 6. Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou
# não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# Com base nas informações acima, faça um algoritmo que leia: o número do empregado
# (código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá
# escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer
# aposentadoria' ou 'Não requerer'.

codigo = int(input("Insira o código do empregado: "))
ano_nasc = int(input("Insira o ano de nascimento do empregado: "))
ano_ingresso = int(input("Insira o ano de ingresso na empresa do empregado: "))

idade = 2024 - ano_nasc
tempo_trabalhado = 2024 - ano_ingresso

print(f"A idade do empregado é de {idade} anos e seu tempo trabalhado é de {tempo_trabalhado} anos.")

if(idade >= 65 or tempo_trabalhado >= 30 or idade >= 60 and tempo_trabalhado >= 25):
    print("Requer aposentadoria!")
else:
    print("Não requer aposentadoria.")
