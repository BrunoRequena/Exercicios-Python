#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

n = 11
while n < 0 or n > 10:
    n = int(input("Digite uma nota de 0  a  10:"))
    print("Valor inválido!")
else:
    print("Nota inserida com sucesso!")

