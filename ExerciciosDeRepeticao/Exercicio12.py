#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo:

while 1==1:
     t = int(input("Por favor, informe a taboada que deseja ver: "))
     n = t
     i = 0
     while (i <= 9):
         i = i + 1
         print(n," x ",i," = ",t)
         t = t+n

