dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM foram rodados? "))
dias_valor = dias * 60
km_valor = km * 0.15

print("O valor da locação do carro é: {:.2f}" .format(dias_valor))
print("O valor a ser pago por KM rodado é de {:.2f}" .format(km_valor))
print("O TOTAL A SER PAGO É DE {:.2f}" .format(dias_valor + km_valor))




