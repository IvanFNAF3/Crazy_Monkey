#класс для поднимаемых предметов
import pygame
ENERGY_COLOR = (255, 255, 255)

class Energy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load("sprites/energy.png")

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y