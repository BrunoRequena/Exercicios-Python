#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print("Este programa mostra se a letra inserida é vogal ou consoante")
l = input("Digite uma letra: ").upper() #upper() para deixar as letras maiúsculas

if (l == "A" or l == "E" or l == "I" or l == "O" or l == "U"):
    print("A letra digitada é vogal")
else:
    print("A letra digitada é consoante")