# Solicita ao usuário que insira o nome da cidade
cidade = input("Digite o nome da cidade: ")

# Converte a cidade para minúsculas e divide em palavras
palavras = cidade.lower().split()

# Verifica se a primeira palavra é "santo"
if palavras[0] == "santo":
    print("O nome da cidade começa com 'SANTO'.")
else:
    print("O nome da cidade não começa com 'SANTO'.")
