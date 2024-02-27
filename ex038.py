def decimal_para_binario(numero):
    return bin(numero)

def decimal_para_octal(numero):
    return oct(numero)

def decimal_para_hexadecimal(numero):
    return hex(numero)

def main():
    numero = int(input("Digite um número inteiro: "))
    print("Escolha a base de conversão:")
    print("1. Binário")
    print("2. Octal")
    print("3. Hexadecimal")
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        print("O número", numero, "em binário é:", decimal_para_binario(numero))
    elif escolha == 2:
        print("O número", numero, "em octal é:", decimal_para_octal(numero))
    elif escolha == 3:
        print("O número", numero, "em hexadecimal é:", decimal_para_hexadecimal(numero))
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()