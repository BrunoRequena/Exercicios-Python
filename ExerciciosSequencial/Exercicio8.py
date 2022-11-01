#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print("Este programa mostra seu salário total referente a suas horas trabalhadas!")

h = float(input("Digite suas horas trabalhadas nesse mês: "))
s = float(input("Digite o quanto você ganha por hora trabalhada: "))

t = h*s

print("Seu salário referente ao número de horas trabalhadas são: R${}".format(t))