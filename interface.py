import pygame

#Класс для кнопки
class Button(pygame.sprite.Sprite):
    def __init__(self, filename, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def change_img(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()