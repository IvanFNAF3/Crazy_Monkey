import pygame

PLATFORM_COLOR = (133, 94, 66)

#класс для платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        #создание изображения для спрайта
        self.image = pygame.Surface((width, height))
        self.image.fill(PLATFORM_COLOR)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y