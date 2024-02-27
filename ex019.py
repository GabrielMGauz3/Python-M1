import random

# Lista de nomes
nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]

# Sorteia um nome aleatório da lista
nome_sorteado = random.choice(nomes)

# Remove o nome sorteado da lista
nomes.remove(nome_sorteado)

# Imprime o nome sorteado
print("O nome sorteado é:", nome_sorteado)

# Imprime a lista atualizada de nomes
print("Lista atualizada de nomes:")
print(nomes)