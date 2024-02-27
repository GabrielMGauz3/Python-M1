# Solicita ao usuário que insira a frase
frase = input("Digite uma frase: ")

# Converte a frase para minúsculas para facilitar a comparação
frase = frase.lower()

# Inicializa as variáveis de contagem e de posição
contagem_a = 0
primeira_posicao = None
ultima_posicao = None

# Percorre a frase para contar a ocorrência da letra "A" e registrar suas posições
for i, letra in enumerate(frase, start=1):
    if letra == "a":
        contagem_a += 1
        if primeira_posicao is None:
            primeira_posicao = i
        ultima_posicao = i

# Exibe o resultado
if contagem_a > 0:
    print("A letra 'A' aparece", contagem_a, "vezes.")
    print("Primeira ocorrência da letra 'A' na posição:", primeira_posicao)
    print("Última ocorrência da letra 'A' na posição:", ultima_posicao)
else:
    print("A letra 'A' não aparece na frase.")


