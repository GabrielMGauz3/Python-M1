import random

# Lista de nomes
nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]

# Embaralha a lista para sortear a ordem
random.shuffle(nomes)

# Imprime a ordem sorteada
print("Ordem sorteada dos nomes:")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")
