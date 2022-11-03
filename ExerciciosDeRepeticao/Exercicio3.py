#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

print("*****LISTA DE PESSOAS******")
nome = str(input("Insira seu nome: "))
while (len(nome) <=3):
        nome = str(input("Insira seu nome: "))

idade = int(input("Insira sua idade: "))
while (idade > 150 or idade < 0):
        idade = int(input("Insira sua idade: "))

S = float(input("Insira seu salário: "))
while (S < 0 ):
        S = float(input("Insira seu salário: "))

sexo = str(input("Insira seu sexo: (F = Feminino / M = Masculino) ").upper())
while sexo != "F" and sexo != "M":
      sexo = str(input("Insira seu sexo: (F = Feminino / M = Masculino) ").upper())

E = str(input("Qual seu estado civil? S = Solteiro(a) / C = Casado(a) / V = Viúvo(a) / D = Divorciado(a)").upper())
while (E != "S" and E != "C" and E != "V" and E != "D"):
    E = str(input("Qual seu estado civil?S = Solteiro(a) / C = Casado(a) / V = Viúvo(a) / D = Divorciado(a)").upper())
