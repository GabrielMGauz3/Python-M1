print("DESCUBRA QUAL É O MAIOR E O MENOR NUMERO")
# Solicita ao usuário que insira três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Encontra o menor número
menor = min(num1, num2, num3)

# Encontra o maior número
maior = max(num1, num2, num3)

# Exibe o resultado
print("O menor número é:", menor)
print("O maior número é:", maior)