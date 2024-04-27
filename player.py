import pygame
from const import*

#класс для игрока
class Player(pygame.sprite.Sprite):

    health = 10
    speed = 5
    is_boosted = False

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = monkey_static

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #компоненты скорости по оси X и Y
        self.x_velocity = 0
        self.y_velocity = 0

        #переменная-флаг для отслеживания в прыжке ли спрайт
        self.on_ground = False

    def update(self):
        # Обновление позиции игрока
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def change_image(self, _image):
        self.image = _image
