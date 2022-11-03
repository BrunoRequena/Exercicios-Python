#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print("Este programa se o valor digitado é positivo ou negativo!")
n = int(input("Digite um número: "))
if n > 0:
    print("O número {} é positivo".format(n))
else:
    print("O número {} é negativo".format(n))
