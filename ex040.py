#ALISTAMENTO MILITAR
#Variaveis de entrada
ano_atual = 2024
ano_nasc = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nasc

if idade < 18:
    print("Você tem apenas {} anos e ainda não pode se alistar".format(idade))
    print("faltam {} anos para seu alistamento obrigatório".format(18 - idade))
elif idade == 18:
    print("Você está com {} anos, compareça ao alistamento obrigatório".format(idade))
else:
    print("Seu periodo de alistamento já passou, você esta com {} anos.".format(idade))
    print("Se passaram {} anos desde o seu alistamento obrigatório".format(idade - 18))


