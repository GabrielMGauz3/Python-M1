#CLASSIFICANDO ATLETAS DE ACORDO COM A IDADE
#Variaveis de entrada
ano_nasc = int(input("Digite o ano de nascimento do atleta: "))
idade = 2024 - ano_nasc

if idade == 9 or idade < 9:
    print("ATLETA MIRIM, idade: {}".format(idade))
elif idade == 14 or idade <14:
    print("ATLETA INFANTIL, idade: {}".format(idade))
elif idade == 19 or idade < 19:
    print("ATLETA JUVENIL, idade: {}".format(idade))
elif idade == 20:
    print("ATLETA SENIOR, idade: {}".format(idade))
else:
    print("ATLETA MASTER, idade: {}".format(idade))

