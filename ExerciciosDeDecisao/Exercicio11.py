#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


print("************ORGANIZAÇÕES TABAJARA!************")
s = float(input("Por favor, insira o valor do seu salário: "))

if s <= 280:
    a = ((s/100)*20)
    st = a + s
    print("Seu salário de R${:.2f} teve um percentual de aumento aplicado de 20% R${:.2f}, resultando no salário de R${:.2f}".format(s,a,st))

elif s > 280 and s <= 700:
    a = ((s / 100) * 15)
    st = a + s
    print("Seu salário de R${:.2f} teve um percentual de aumento aplicado de 15% R${:.2f}, resultando no salário de R${:.2f}".format(s,a,st))

elif s > 700 and s <= 1500:
    a = ((s / 100) * 10)
    st = a + s
    print("Seu salário de R${:.2f} teve um percentual de aumento aplicado de 10% R${:.2f}, resultando no salário de R${:.2f}".format(s,a,st))

else:
    a = ((s / 100) * 5)
    st = a + s
    print("Seu salário de R${:.2f} teve um percentual de aumento aplicado de 5% R${:.2f}, resultando no salário de R${:.2f}".format(s,a,st))
