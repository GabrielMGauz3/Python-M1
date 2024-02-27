print("GERENCIADOR DE PAGAMENTO")
print("------------------------")
#Variaveis de entrada:
valor = float(input("Valor do produto: R$ "))
print("Escolha seu metodo de pagamento:\n1 - À VISTA \n2 - À VISTA NO CARTÃO \n3 - Até 2x \n4 - 3x ou mais ")
metodo = (int(input("Escolha seu método de pagamento: ")))
#Condicionais
if metodo == 1:
    print("À VISTA R$ {:.2f}".format(valor * 10 / 100))
elif metodo == 2:
    print("Á VISTA no cartão R$ {:.2f}".format(valor * 5 / 100))
elif metodo == 3:
    print("2x no cartão R$ {:.2f} / 2x de R$ {:.2f}".format(valor, valor / 2))
elif metodo == 4:
    parcelas = int(input("Em quantas vezes deseja fazer: "))
    print("Em {}x R$ {:.2f}, VALOR TOTAL R$ {:.2f}" .format(parcelas, (valor + (valor / 100 * 20)) / parcelas, valor + (valor / 100 * 20)))
else:
    print("OPÇÂO INVÁLIDA")
