import pygame

pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\luvison\Documents\estudos\python\aula 8\desafio21.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)