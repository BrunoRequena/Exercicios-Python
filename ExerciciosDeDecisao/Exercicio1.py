#Faça um Programa que peça dois números e imprima o maior deles.

print("Este programa mostra o maior número digitado!")
n1 = int(input("Digite 1º número: "))
n2 = int(input("Digite 2º número: "))
if n1 > n2:
    print(" {} é maior que {}".format(n1, n2))
else:
    print(" {} é maior que {}".format(n2, n1))

