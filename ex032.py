print("CALCULE O VALOR DA SUA PASSAGEM DE ONIBUS")
#Variavel para distancia em km da viagem
viagem = int(input("Insira a distancia em KM até seu destino: "))
#condicional
if viagem > 200:
    print("A valor cobrado em viagens com mais de 200km é de 0,45 centavos por km")
    valor2 = viagem * 0.45
    print("O valor cobrado da sua passagem é de R$ {:.2f}".format(valor2))
else:
    print("A Valor cobrado em viagens até 200Km é de 0,50 centavos por km")
    valor1 = viagem * 0.50
    print("O valor da sua passagem é de {:.2f} reais".format(valor1))

