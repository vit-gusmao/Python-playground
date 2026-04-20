import pygame

pygame.init()
pygame.mixer.init()

print("'pygame.mixer.music.load(arquivo)' = carrega um áudio.\n")
pygame.mixer.music.load("musica.mp3")


print("'pygame.mixer.music.play()' = toca o áudio.\n")
pygame.mixer.music.play()


print("'pygame.mixer.music.stop()' = para o áudio.\n")
# pygame.mixer.music.stop()


print("'pygame.mixer.music.pause()' = pausa.\n")
# pygame.mixer.music.pause()


print("'pygame.mixer.music.unpause()' = continua.\n")
# pygame.mixer.music.unpause()


print("'pygame.mixer.music.set_volume(0.0 a 1.0)' = volume.\n")
pygame.mixer.music.set_volume(0.5)


print("'pygame.mixer.music.get_busy()' = verifica se está tocando.\n")
print(pygame.mixer.music.get_busy())


input("Pressione ENTER para sair...")