#COMPARANDO NUMEROS
#Variaveis de entrada
n1 = float(input("Digite o primeiro numero para comparação -> "))
n2 = float(input("Digite o segundo numero para comparação -> "))
#Condicionais para maior, menor, igual
if n1 > n2:
    print("O primeiro numero {} é maior que o segundo numero {}".format(n1, n2))
elif n2 > n1:
    print("O segundo numero {} é maior que o primeiro numero {}".format(n2, n1))
else:
    print("O primeiro numero {} e o segundo numero {} são IGUAIS".format(n1, n2))



