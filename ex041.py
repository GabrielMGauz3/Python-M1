#ANALISE DE MÉDIA DE UM ALUNO
#Variaveis de entrada de notas
nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Sua nota é {}, Infelizmente você foi REPROVADO".format(media))

elif media == 5 or media < 6.9:
    print("Sua nota é {}, Infelizmente você está de RECUPERAÇÂO".format(media))

else:
    print("PARABÉNS, Você foi APROVADO")
    print("Sua media é {}".format(media))
