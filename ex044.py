print("CALCULO DE IMC")
#Variaveis de entrada de dados
peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))
imc = peso / (alt ** 2)
#Condicionais
if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc == 25 or imc > 18.5:
    print("PESO IDEAL")
elif imc == 30 or imc > 25:
    print("SOBREPESO")
elif imc == 40 or imc > 30:
    print("OBESIDADE")
else:
    print("OBESIDADE MORBIDA")

