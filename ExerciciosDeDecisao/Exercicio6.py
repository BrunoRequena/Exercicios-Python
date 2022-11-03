#Faça um Programa que leia três números e mostre o maior deles.

print("Este programa lê três números e mostra o maior entre eles!")

n1 = int(input("Digite 1º número: "))
n2 = int(input("Digite 2º número: "))
n3 = int(input("Digite 3ª número: "))

if n1 > n2 and n1 > n3:
    print("O maior número inserido é: {}".format(n1))
elif n2 > n1 and n2> n3:
    print("O maior número inserido é: {}".format(n2))
else:
    print("O maior número inserido é: {}".format(n3))