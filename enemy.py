import pygame
import random
from const import*

ENEMY_COLOR = (105, 105, 105)

#класс для патрулирующих врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #создание изображения для спрайта
        self.image = bull

        #начальная позиция по Х, нужна для патрулирования
        self.x_start = x
        #выбор направления начального движения
        self.direction = random.choice([-1, 1])

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #компоненты скорости по оси Х и Y
        self.x_velocity = 1
        self.y_velocity = 0
    
    def update(self):
        #если расстояние от начальной точки превысило 50
        #то меняем направление
        if abs(self.x_start - self.rect.x) > 50:
            self.direction *= -1

        #движение спрайта по оси Х
        self.rect.x += self.x_velocity * self.direction
