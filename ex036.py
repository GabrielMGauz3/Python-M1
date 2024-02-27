print("SAIBA SE AS RETAS PODEM OU NAO SER UM TRIANGULO")

# Variaveis solicitam ao usuário que insira os comprimentos das 3 retas
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))
# Condicional Verifica se as medidas podem formar um triângulo
#verifica se cada uma das três medidas é menor que a soma das outras duas medidas
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As medidas podem formar um triângulo.")
else:
    print("As medidas não podem formar um triângulo.")

    