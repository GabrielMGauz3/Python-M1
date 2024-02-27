import random
n = int(input("Receba um número de participantes para um sorteio randômico: "))

sorteado = random.randint(1, n)

print("O Vencedor é {}".format(sorteado))

