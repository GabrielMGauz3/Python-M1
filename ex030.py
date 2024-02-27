#Variavel de entrada da velocidade
velocidade = int(input("Digite a velocidade em km que você costuma dirigir: "))
#condição para aplicação de multa
if velocidade > 80:
    print("Você excedeu o limite de velocidade e será punido")
    print("o valor da multa é 7 reais por km excedente")
    #Calculo do valor da multa
    multa = (velocidade - 80)*7
    print("Sua multa é de {} reais".format(multa))
else:
    print("Muita bem, você não excedeu o limite de velocidade")



