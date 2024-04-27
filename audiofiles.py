import pygame
pygame.mixer.init()

lose = pygame.mixer.Sound("sounds/game_over.mp3")
win = pygame.mixer.Sound("sounds/you_win.mp3")
coin_sound = pygame.mixer.Sound("sounds/coin.mp3")
click = pygame.mixer.Sound("sounds/click.mp3")


pygame.mixer.music.load("sounds/untitled.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
#untitled.mp3




