print("CALCULE O AUMENTO DE SALARIO")
#Variavel de entrada para o salario atual
salario = float(input("Digite o salário para saber seu respectivo aumento: "))
#Condional
if (salario > 1250) or (salario == 1250):
    print("Para salarios maiores ou iguais a 1250,00 reais o aumento é de 10%")
    aumento1 = (salario * 10)/ 100 + salario
    print("O salario com aumento é de {:.2f} reais".format(aumento1))
else:
    print("Para salarios menores 1250,00 reais o aumento é de 15%")
    aumento2 = (salario * 15) / 100 + salario
    print("O salario com aumento é de {:.2f} reais".format(aumento2))


