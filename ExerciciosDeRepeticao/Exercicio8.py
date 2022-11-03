#Faça um programa que leia 5 números e informe a soma e a média dos números.

n = []
i = 0

soma = 0
while i < 5:
    n.append(int(input("Insira um número: ")))
    i = i+1

n1 = len(n)
for i in range(n1):
    soma += n[i]
print("A soma dos números inseridos é de : ",soma)