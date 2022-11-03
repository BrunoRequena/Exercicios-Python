#Faça um Programa que leia três números e mostre o maior e o menor deles.

print("Este programa lê três números e mostra o maior e o menor inserido!")

n1 = int(input("Insira 1º número: "))
n2 = int(input("Insira 2º número: "))
n3 = int(input("Insira 3º número: "))

if n1 > n2 and n1 > n3:
    print("O número {} é o maior!".format(n1))
elif n2 > n1 and n2 > n3:
    print("O número {} é o maior!".format(n2))
else:
    print("O número {} é o maior!".format(n3))

if n1 < n2 and n1 < n3:
    print("O número {} é o menor!".format(n1))
elif n2 < n1 and n2 < n3:
    print("O número {} é o menor!".format(n2))
else:
    print("O número {} é o menor!".format(n3))



