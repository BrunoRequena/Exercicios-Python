#Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou
# "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Qual turno você estuda?")
t = input(" M = matutino / V = vespertino / N = noturno").upper()

if t == "M":
    print("BOM DIA!")
elif t == "V":
    print("BOA TARDE!")
elif t == "N":
    print("BOA NOITE")
else:
    print("VALOR INVÁLIDO!")
