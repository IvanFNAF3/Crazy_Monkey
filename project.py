#HJRGFKLDRJLFKRD:LF
#;de;kf
#АКИМОВ ФОРЕВЕР
#kf;jsdflksdjfklj
#zvbif
#rfvsojxtrvbi,thnf
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA#
####################################################################################
# Данный код представляет собой каркас для игры в жанре платформер                 #
# В нем определены: классы главного героя, врагов, собираемых предметов и платформ #
# управление с помощью клавиатуры, проверка коллизий объектов                      #
# Проект можно запустить для демонстрации функционала                              #
####################################################################################

################################################################
#При запуске:                                                  #
# синие элементы - платформы,                                  #
# красный элемент - враг,                                      #
# зеленый элемент - игрок,                                     #
# желтый элемент - собираемый предмет                          #
#                                                              #
#Управление: стрелки клавиатуры для движения, пробел для прыжка#
################################################################

#подключние бибилиотек
import pygame
from audiofiles import*
from simple_platform import*
from enemy import*
from simple_platform import*
from enemy import*
from coin import*
from player import*
from energy import*


#инициализация Pygame
pygame.init()

#константы-параметры окна
WIDTH = 1920
HEIGHT = 1080
#константы-цвета
BG = (34, 139, 34)
SCORE_COLOR = (0, 0, 0)
speed = 5
maxReload = 5

#функция для проверки коллизий c платформой
def check_collision_platforms(object, platform_list):
    #перебираем все платформы из списка (не группы спрайтов)
    for platform in platform_list:
        if object.rect.colliderect(platform.rect):
            if object.y_velocity > 0: # Если спрайт падает
                #меняем переменную-флаг
                object.on_ground = True
                #ставим его поверх платформы и сбрасываем скорость по оси Y
                object.rect.bottom = platform.rect.top
                object.y_velocity = 0
            elif object.y_velocity < 0: # Если спрайт движется вверх
                #ставим спрайт снизу платформы
                object.rect.top = platform.rect.bottom
                object.y_velocity = 0
            elif object.x_velocity > 0: # Если спрайт движется вправо
                #ставим спрайт слева от платформы
                object.rect.right = platform.rect.left
            elif object.x_velocity < 0: # Если спрайт движется влево
                #ставим спрайт справа от платформы
                object.rect.left = platform.rect.right

#функция проверки коллизии выбранного объекта с объектами Enemies
def check_collision_enemies(object, enemies_list):
    #в списке проверяем
    for enemy in enemies_list:
        #при коллизии
        if object.rect.colliderect(enemy.rect):
            #враг умирает
            enemy.kill()

#проверка 
def check_collision_collectibles(object):
    #делаем видимыми объекты для подбора в игре и очки
    global collectibles_list
    global score
    #если object касается collictible 
    for collectible in collectibles_list:
        if object.rect.colliderect(collectible.rect):
            #убираем этот объект из всех групп
            collectible.kill()
            #убираем этот объект из списка (чтобы не было проверки коллизии)
            collectibles_list.remove(collectible)
            #прибавляем одно очко
            score += 1

def check_collision_energies(object):
    global energies_list
    global score
    global speed
    global reload
    for energy in energies_list:
        if object.rect.colliderect(energy.rect):
            energy.kill()
            energies_list.remove(energy)
            speed += 5
            reload = maxReload


#создаем экран, счетчик частоты кадров и очков
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
score = 0
reload = 0

#создаем игрока, платформы, врагов и то, что будем собирать в игре
player = Player(50, 50)
platforms_list = [Platform(0, HEIGHT-25, WIDTH, 50), Platform(50, 150, 100, 20), Platform(100, 350, 100, 20), Platform(250, 170, 100, 20), Platform(500, 170, 350, 20)]
enemies_list = [Enemy(120, 315)]
collectibles_list = [Collectible(280, 135)]
energies_list = [Energy(320, 135)]

#счёт игры
font = pygame.font.Font(None, 36) # создание объекта, выбор размера шрифта
score_text = font.render("Счёт: 0", True, SCORE_COLOR) # выбор цвета и текст
score_rect = score_text.get_rect() # создание хитбокса текста
score_rect.topleft = (WIDTH - 100, 20) # расположение хитбокса\текста на экране

#создаем групп спрайтов
player_and_platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
energies = pygame.sprite.Group()

#в трех циклах добавляем объекты в соответствующие группы
for i in enemies_list:
    enemies.add(i)

for i in platforms_list:
    player_and_platforms.add(i)

for i in collectibles_list:
    collectibles.add(i)

for i in energies_list:
    energies.add(i)

#отдельно добавляем игрока
player_and_platforms.add(player)

#игровой цикл
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #проверяем нажатие на клавиши для перемещения
    keys = pygame.key.get_pressed()
    player.x_velocity = 0
    if keys[pygame.K_LEFT]:
        player.x_velocity = -speed
    if keys[pygame.K_RIGHT]:
        player.x_velocity = speed
    #условие прыжка более сложное
    if keys[pygame.K_SPACE] and player.on_ground == True:
        player.y_velocity = -9
        player.on_ground = False

    #гравитация для игрока
    player.y_velocity += 0.3 

    #обновляем значения атрибутов игрока и врагов
    player.update()
    enemies.update()

    #отрисовываем фон, платформы, врагов и собираемые предметы
    screen.fill(BG)
    player_and_platforms.draw(screen)
    enemies.draw(screen)
    collectibles.draw(screen)
    energies.draw(screen)

    #проверяем все возможные коллизии
    check_collision_platforms(player, platforms_list)
    check_collision_enemies(player, enemies_list)
    check_collision_collectibles(player)
    check_collision_energies(player)

    #уменьшаем перезарядку если есть
    if(reload > 0):
        reload -= 1/60
    elif(reload <= 0):
        speed = 5


    #обновление счёта на экране
    score_text = font.render("Счёт: " + str(score), True, SCORE_COLOR)
    screen.blit(score_text, score_rect)
    #обновление экрана и установка частоты кадров
    pygame.display.update()
    clock.tick(60)

pygame.quit()