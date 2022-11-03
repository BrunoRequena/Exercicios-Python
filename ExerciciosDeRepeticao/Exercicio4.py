#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de
#3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
# ou iguale a população do país B, mantidas as taxas de crescimento.

pa = 80000
pb = 200000
a = 0
while pa < pb:
    pa +=round((pa*3.0)/100)
    pb +=round((pb*1.5)/100)
    a = a+1
print("Levará {}anos para que a população A ser maior que a população B\nPopulação A = {} \nPopulação B = {}".format(a,pa,pb))