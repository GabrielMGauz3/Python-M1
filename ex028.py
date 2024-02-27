# Solicita ao usuário que insira o nome completo
nome_completo = input("Digite o nome completo: ")

# Divide o nome completo em palavras
palavras = nome_completo.split()

# Pega o primeiro nome (primeira palavra)
primeiro_nome = palavras[0]

# Pega o último nome (última palavra)
ultimo_nome = palavras[-1]

# Exibe o resultado
print("Primeiro nome:", primeiro_nome)
print("Último nome:", ultimo_nome)