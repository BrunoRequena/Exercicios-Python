#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print("Este programa transforma graus Celsius em Fahrenheit!")
c = float(input("Digite uma temperatura em Celsius: "))
f = (c*(9/5)) + 32

print("A temperatura convertidad de Celsius para Fahrenheit é de: {:.1f}ºF".format(f))