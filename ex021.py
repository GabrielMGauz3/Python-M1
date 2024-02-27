import pygame

# Inicializa o pygame
pygame.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("testesound.mp3")

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música está sendo reproduzida
while pygame.mixer.music.get_busy():
    continue