import pygame


#Здесь все спрайты игры в отдельных переменных для удобства
bg_gameplay = pygame.image.load("sprites/BG.jpg")
bg_menu = pygame.image.load("sprites/BG_menu.png")
bg_aboutgame = pygame.image.load("sprites/BG_aboutgame.png")
monkey_static = pygame.image.load("sprites/monkey_static.png")
monkey_static_r = pygame.transform.flip(monkey_static, True, False)
monkey_crazy = pygame.image.load("sprites/monkey_energy.png")
bull = pygame.image.load("sprites/bull.png")
