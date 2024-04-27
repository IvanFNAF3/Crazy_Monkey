import pygame

PORTAL_COLOR = (0, 206, 209)

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        #создание изображения для спрайта
        self.image = pygame.Surface((width, height))
        self.image.fill(PORTAL_COLOR)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y