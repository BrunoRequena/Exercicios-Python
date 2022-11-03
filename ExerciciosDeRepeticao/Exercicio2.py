#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

print("*******REALIZE SEU CADASTRO AQUI********")

l = str(input("LOGIN: "))
s = str(input("SENHA: "))

while l == s:
    print("ERRO: login e senha não podem ser iguais, tente novamente!")
    l = str(input("LOGIN: "))
    s = str(input("SENHA: "))
else:
    print("CADASTRO REALIZADO COM SUCESSO!")