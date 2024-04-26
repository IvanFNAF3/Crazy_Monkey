#класс для поднимаемых предметов
import pygame
GOLD = (255, 215, 0)

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        self.image = pygame.Surface((16, 16))
        self.image.fill(GOLD)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y