#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e
# que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.

print("******Iremos te auxiliar com a folha de pagamento!*******")

sh = float(input("Por favor, insira o valor ganho por horas trabalhadas: "))
h = float(input("Por favor, insira o número de horas trabalhadas no mês: "))

sb = sh * h
inss = ((sb/100)*10)
fgts = ((sb/100)*11)
sl = sb-inss-fgts

if sb <= 900:
    t = inss + fgts
    print("Salário bruto     : R${:.2f} \n(-) IR (0%)    : R$----- \n(-) INSS (10%)     : R${:.2f} "
          "\n(-) FGTS (11%)     : R${:.2f} \nTotal de descontos      : R${:.2f} \nSalário Liguido     : R${:.2f}".format(sb,inss,fgts,t,sl))
elif sb > 900 and sb <= 1500:
    ir = (sb / 100) * 5
    t = inss + fgts + ir
    print("Salário bruto     : R${:.2f} \n(-) IR (5%)    : R${:.2f} \n(-) INSS (10%)     : R${:.2f} "
          "\n(-) FGTS (11%)     : R${:.2f} \nTotal de descontos      : R${:.2f} \nSalário Liguido     : R${:.2f}".format(sb,ir, inss, fgts, t, sl))
elif sb > 1500 and sb <= 2500:
    ir = (sb / 100) * 10
    t = inss + fgts + ir
    print("Salário bruto     : R${:.2f} \n(-) IR (10%)    : R${:.2f} \n(-) INSS (10%)     : R${:.2f} "
          "\n(-) FGTS (11%)     : R${:.2f} \nTotal de descontos      : R${:.2f} \nSalário Liguido     : R${:.2f}".format(sb,ir, inss, fgts, t, sl))
else :
    ir = (sb / 100) * 20
    t = inss + fgts + ir
    print("Salário bruto     : R${:.2f} \n(-) IR (20%)    : R${:.2f} \n(-) INSS (10%)     : R${:.2f} "
          "\n(-) FGTS (11%)     : R${:.2f} \nTotal de descontos      : R${:.2f} \nSalário Liguido     : R${:.2f}".format(sb, ir, inss, fgts, t, sl))