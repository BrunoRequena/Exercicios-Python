#Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

print('Este programa mostra a temperatura convertida de Fahrenheit para Celsius!')

f = float(input("Digite o valor da temperatura em Fahrenheit: "))
c = 5*((f-32)/9)

print('A temperatura convertida em Celsius é {:.1f}ºC'.format(c))