#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
# usando a seguinte fórmula: (72.7*altura) - 58

print("Digite sua altura e direi seu peso ideal!")
a = float(input("Digite sua altura: "))
p = (72.7*a) - 58

print("Seu peso ideal a partir da sua altura {}m é: {:.2f}Kg".format(a, p))