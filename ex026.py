# Solicita ao usuário que insira o nome
nome = input("Digite o nome: ")

# Converte o nome para minúsculas
nome_min = nome.lower()

# Verifica se "silva" está presente no nome
if "silva" in nome_min:
    print("O nome contém 'Silva'.")
else:
    print("O nome não contém 'Silva'.")