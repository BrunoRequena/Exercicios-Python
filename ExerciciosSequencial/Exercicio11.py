#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

print("Este programa te dara três resultados!")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
nReal= int(input("Digite um número real: "))
r1 = n1 * 2 * (n2 / 2)
r2 = n1 * 3 + nReal
r3 = nReal ** 3

print("O produto do dobro do primeiro número com metade do segundo é: ", r1)
print("A soma do triplo do primeir número com o terceiro é: ", r2)
print("O terceiro número elevado ao cubo é: ", r3)
