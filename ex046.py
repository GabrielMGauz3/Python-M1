import random
import time
print(" JOGO DE PEDRA, PAPEL, TESOURA")
print("------------------------------")
#FUNÇÃO DO GAME
opcoes = ['pedra', 'papel', 'tesoura']
#Variavel de entrada
escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
escolha_computador = random.choice(opcoes)

print("JO")
time.sleep(0.5)
print("KEN")
time.sleep(0.5)
print("PO !")
time.sleep(0.5)
print("-=-" * 11)
print("Você escolheu:", escolha_usuario)
print("O computador escolheu:", escolha_computador)

if escolha_usuario == escolha_computador:
    print("Empate!")
elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
        (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
        (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
    print("Você ganhou!")
else:
    print("Você perdeu!")
print("-=-" * 11)

