'''
7. As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
critério, baseado no salário atual:
salários até R$ 280,00 (incluindo): aumento de 20%
salários entre R$ 280,00 e R$ 700,00: aumento de 15%
salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
salários de R$ 1500,00 em diante: aumento de 5%
    Após o aumento ser realizado, informe na tela:
    • salário antes do reajuste;
    • percentual de aumento aplicado;
    • valor do aumento;
    • novo salário, após o aumento.
'''

salario = float(input("Insira o salário: "))

if(salario < 280):
    print(f"O salario de {salario} reajustado com aumento de 20%, equivalente a {salario*0.2}, é igual a {salario + (salario*0.2)}",)

elif(salario >= 280 and salario < 700):
    print(f"O salario de {salario} reajustado com aumento de 15%, equivalente a {salario*0.15}, é igual a {salario + (salario*0.15)}",)

elif(salario >= 700 and salario < 1500):
    print(f"O salario de {salario} reajustado com aumento de 10%, equivalente a {salario*0.1}, é igual a {salario + (salario*0.1)}",)

else:
    print(f"O salario de {salario} reajustado com aumento de 5%, equivalente a {salario*0.05}, é igual a {salario + (salario*0.05)}",)