#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

print("Este programa lhe ajudará a escolher o produto mais barato para compra!")

p1 = float(input("Insira o valor do 1º produto: "))
p2 = float(input("Insira o valor do 2º produto: "))
p3 = float(input("Insira o valor do 3º produto: "))

if p1 < p2 and p1 < p3:
    print("O 1º produto custa R${} sendo o mais barato!".format(p1))
elif p2 < p1 and p2 < p3:
    print("O 2º produto custa R${} sendo o mais barato!".format(p2))
else:
    print("O 3º produto custa R${} sendo o mais barato!".format(p3))
