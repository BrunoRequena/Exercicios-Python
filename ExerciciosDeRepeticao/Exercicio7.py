#Faça um programa que leia 5 números e informe o maior número.

n = []
i = 0
while i < 5:
    n.append(input("Insira um número: "))
    i = i+1
else:
    print(sorted(n, reverse=True)[0])