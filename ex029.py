import random
#Computador escolhe um numero
print("TENTE ADVINHAR O NUMERO DE 1 a 10 ESCOLHIDO PELO COMPUTADOR")
numero = random.randint(1, 10)
#Print de verificação do número escolhido
print(numero)
#variavel de entrade para palpite
chute = int(input("Seu palpite é: "))
#condição
if chute == numero:
    print("PARABÉNS FOI UM CHUTE CERTEIRO")
else:
    print("VOCÊ ERROU =( ")
