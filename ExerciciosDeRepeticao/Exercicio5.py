#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

pa = float(input("Insira o número de habitantes na cidade A: "))
pb = float(input("Insira o número de habitantes na cidade B: "))
a = 0
t1 = float(input("Insira a taxa de crescimento da população A: "))
t2 = float(input("Insira a taxa de crescimento da população B: "))
while pa < pb:
    pa +=round((pa*t1)/100)
    pb +=round((pb*t2)/100)
    a = a+1
print("Levará {} anos para que a população A ser maior que a população B\nPopulação A = {} \nPopulação B = {}".format(a,pa,pb))
