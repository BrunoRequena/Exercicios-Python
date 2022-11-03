#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

s = input("Digite F para Feminino ou M para Masculino: ")
if s == "F" or s == "f":
    print("Feminino")
elif s == "M" or s == "m":
    print("Masculino")
else:
    print("Sexo Inválido")