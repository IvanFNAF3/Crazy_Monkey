#класс для поднимаемых предметов
import pygame

class Energy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #создание изображения для спрайта
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/energy.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))