#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Insira um número: "))
n2 = int(input("Insira um número maior que anterior: "))
s = 0

while (n1<n2-1):
    n1 = n1+1
    print(n1)
    s = n1 + s
print("A soma de todos os números é: ", s)
