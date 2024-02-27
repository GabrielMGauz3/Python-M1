# Solicita ao usuário que insira um número entre 0 e 9999
numero = int(input("Digite um número entre 0 e 9999: "))

# Converte o número para uma string
numero_str = str(numero)

# Imprime cada dígito separadamente
print("Milhar:", numero_str[0])
print("Centena:", numero_str[1])
print("Dezena:", numero_str[2])
print("Unidade:", numero_str[3])