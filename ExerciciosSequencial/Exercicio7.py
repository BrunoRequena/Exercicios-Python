#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Este programa calcula a área de um quadrado e te mostra o dobro desta área!")

l = float(input('Digite a medida de um lado do quadrado: '))
a = l*l
d = a*2
print("A área do quadrado é {}m² e o dobro da área é {}m²".format(a, d))
