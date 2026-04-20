import pygame

print("Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.\n")

pygame.init()
print(f"Tocando agora:'Arctic Monkeys - Fluorescent Adolescent'")
pygame.mixer.music.load('Fluorescent Adolescent.mp3')
pygame.event.wait()

input("\nAperte qualquer coisa para fechar...")