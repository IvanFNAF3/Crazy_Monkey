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

#подключение всех бибилиотек
import pygame
from audiofiles import*
from platforms import*
from enemy import*
from coin import*
from player import*
from energy import*
from const import*
from interface import*
from init import*
from portal import*


#инициализация Pygame
pygame.init() 

#константы-параметры окна
WIDTH = 1920
HEIGHT = 1080

#константы-цвета
BG = (34, 139, 34)
SCORE_COLOR = (0, 0, 0)

#Создаём меню
def menu():
    #Создаём глобальные переменнные
    global is_music_playing
    global is_skin_miko
    is_skin_miko = False

    #отключаем все звуки и включаем музыку
    pygame.mixer.music.play(-1)
    pygame.mixer.pause()

    #отрисовываем фон меню
    screen.blit(bg_menu, (0, 0))

    #Добавляем кнопки играть, выход, об игре, скин обезьяны, скин мико
    start_button = Button("sprites/play_ui_1.png", 900, 745)
    exit_button = Button("sprites/exit_ui.png", 910, 981)
    aboutgame_button = Button("sprites/aboutgame_ui.png", 910, 875)
    skinmonkey_button = Button("sprites/monkey_static_but_pressed.png", 60, HEIGHT - 170)
    skinmiko_button = Button("sprites/miko_but.png", 200, HEIGHT - 170)

    #Добавляем кнопки вкл/выкл звук
    if is_music_playing == True: #Если музыка играет, то выбранная кнопка вкл
        msc_off_button = Button("sprites/msc_off_ui.png", 60, HEIGHT - 60)
        msc_on_button = Button("sprites/msc_on_ui_selected.png", 200, HEIGHT - 60)
    else: #Иначе, выбрана кнопка выкл
        msc_off_button = Button("sprites/msc_off_ui_selected.png", 60, HEIGHT - 60)
        msc_on_button = Button("sprites/msc_on_ui.png", 200, HEIGHT - 60)

    
    #Вносим все кнопки в список
    buttons = [start_button, exit_button, msc_on_button, msc_off_button,skinmiko_button , aboutgame_button, skinmonkey_button]

    #Инициализируем список
    init_but(screen, buttons)

    #Обновляем монитор
    pygame.display.update()

    #Код идущий каждый кадр
    while True:
        #Отрисовываем все кнопки и обновляем дисплей
        init_but(screen, buttons)
        pygame.display.update()

        #Проверка выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Проверка нажатия лкм
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_button.rect.collidepoint(x, y): #Кнопка играть
                    click.play() #Звук клика
                    game() #Переход в игру
                elif exit_button.rect.collidepoint(x, y): #Кнопка выхода
                    click.play() #Звук клика
                    pygame.quit() #Выход из игры
                    quit()
                elif msc_off_button.rect.collidepoint(x, y): #Кнопка выкл музыку
                    click.play() #Звук клика
                    pygame.mixer.music.set_volume(0.0) #Ставим громкость на 0
                    msc_off_button.change_img("sprites/msc_off_ui_selected.png") 
                    msc_on_button.change_img("sprites/msc_on_ui.png")
                    is_music_playing = False 
                elif msc_on_button.rect.collidepoint(x, y): #Кнопка вкл музыку
                    click.play() #Звук клика
                    pygame.mixer.music.set_volume(0.4) #Ставим громкость на 0.4
                    msc_off_button.change_img("sprites/msc_off_ui.png") 
                    msc_on_button.change_img("sprites/msc_on_ui_selected.png")
                    is_music_playing = True
                elif aboutgame_button.rect.collidepoint(x, y): #кнопка об игре
                    click.play() #Звук клика
                    tutorial()
                elif skinmiko_button.rect.collidepoint(x, y): #Кнопка скин мико
                    click.play() #Звук клика
                    is_skin_miko = True #Устанавливаем скин мико
                    skinmiko_button.change_img("sprites/miko_but_pressed.png") 
                    skinmonkey_button.change_img("sprites/monkey_static_but.png")
                elif skinmonkey_button.rect.collidepoint(x, y): #Кнопка скин обезьяны
                    click.play() #Звук клика
                    is_skin_miko = False #Устанавливаем скин обезьянки
                    skinmiko_button.change_img("sprites/miko_but.png") 
                    skinmonkey_button.change_img("sprites/monkey_static_but_pressed.png")

def tutorial(): #Окно об игре
    global is_music_playing
    screen.blit(bg_aboutgame, (0, 0)) #Ставим фон

    #Кнопка закрытия
    close_button = Button("sprites/exit_menu_ui.png", 900, 800)

    buttons = [close_button]

    init_but(screen, buttons)
    pygame.display.update()

    while True:
        init_but(screen, buttons)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if close_button.rect.collidepoint(x, y):
                    click.play()
                    menu()

def youwin(): #Окно победы
    global is_music_playing
    pygame.mixer.music.stop()
    if is_music_playing == True:
        win.play() #Музыка для победы
    screen.blit(bg_youwin, (0,0))

    #Кнопки да и нет
    yes_button = Button("sprites/yes_ui.png", 750, 800)
    no_button = Button("sprites/no_ui.png", 1000, 800)

    buttons = [yes_button, no_button]
    init_but(screen, buttons)

    while True:
        init_but(screen, buttons)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if yes_button.rect.collidepoint(x, y):
                    click.play()
                    game()
                elif no_button.rect.collidepoint(x, y):
                    click.play()
                    menu()

def gameover(): #Окно поражения (тоже самое что и с победой)
    global is_music_playing
    pygame.mixer.music.stop()
    if is_music_playing == True:
        lose.play()
    screen.blit(bg_gameover, (0,0))

    yes_button = Button("sprites/yes_ui.png", 750, 800)
    no_button = Button("sprites/no_ui.png", 1000, 800)

    buttons = [yes_button, no_button]
    init_but(screen, buttons)

    while True:
        init_but(screen, buttons)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if yes_button.rect.collidepoint(x, y):
                    click.play()
                    game()
                elif no_button.rect.collidepoint(x, y):
                    click.play()
                    menu()


#функция для проверки коллизий c горизонтальной платформой
def check_h_collision_platforms(object, platform_list):
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
                object.y_velocity = 0.6

#функция для проверки коллизий c вертикальной платформой
def check_v_collision_platforms(object, platform_list):
    for platform in platform_list:
        if object.rect.colliderect(platform.rect):
            object.y_velocity = 0.6
            if object.x_velocity > 0: # Если спрайт движется вправо
                #ставим спрайт слева от платформы
                object.rect.right = platform.rect.left
            elif object.x_velocity < 0: # Если спрайт движется влево
                #ставим спрайт справа от платформы
                object.rect.left = platform.rect.right

#функция для проверки коллизий c порталом
def check_collision_portal(object, portal):
    if object.rect.colliderect(portal.rect):
        youwin() #Победа

#функция проверки коллизии выбранного объекта с объектами Enemies
def check_collision_enemies(object, enemies_list):
    #running делаем видимой внутри функции чтобы было возможно
    #завершить игру
    global running
    #в списке проверяем
    for enemy in enemies_list:
        #при коллизии
        if object.rect.colliderect(enemy.rect):
            #Если взят энергетик, то враг умирает
            if reload_energy > 0:
                kill_sound.play()
                enemy.kill()
                enemies_list.remove(enemy)
            #Иначе мы теряем одну жизнь
            else:
                if object.cooldown <= 0:
                    damage_sound.play()
                    object.health -= 1
                    if(object.health <= 0):
                        gameover()
                    object.cooldown = object.maxCooldown
                

#проверка 
def check_collision_collectibles(object, collectibles_list):
    #делаем видимыми объекты для подбора в игре и очки
    global score
    global has_portal
    #если object касается collictible 
    for collectible in collectibles_list:
        if object.rect.colliderect(collectible.rect):
            #Звук подбирания монетки
            coin_sound.play()
            #убираем этот объект из всех групп
            collectible.kill()
            #убираем этот объект из списка (чтобы не было проверки коллизии)
            collectibles_list.remove(collectible)
            #прибавляем одно очко
            score += 1
            if(score == 15):
                global portal 
                portal_sound.play()
                portal = Portal(60, 225, 20, 125)
                has_portal = True

#функция для проверки коллизий c энергетиком
def check_collision_energies(object, energies_list, _maxReloadEnergy):
    global speed
    global reload_energy
    for energy in energies_list:
        if object.rect.colliderect(energy.rect):
            #Мы становимся быстрее и больше из-за нового спрайта
            energy.kill()
            energy_sound.play()
            energies_list.remove(energy)
            object.speed = 10
            reload_energy = _maxReloadEnergy
            if(is_skin_miko == True):
                object.change_image(miko_energy)
            else:
                object.change_image(monkey_crazy)


#создаем экран, счетчик частоты кадров и очков
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
is_music_playing = True

def game(): #Окно игры
    #Переменные
    global score
    score = 0
    global is_music_playing
    global reload_energy
    global has_portal
    has_portal = False
    global timer
    timer = 35
    reload_energy = 0
    maxReload_energy = 5

    #Включаем музыку
    pygame.mixer.stop()
    if is_music_playing == True:
        pygame.mixer.music.play(-1)

#создаем игрока, платформы, врагов и то, что будем собирать в игре
    player = Player(50, 50)
    #включаем выбранный скин
    if(is_skin_miko):
        player_skin = miko_static
    else:
        player_skin = monkey_static

    global player_img
    player_img = player_skin

    player.image = player_skin
    screen.blit(player.image, player.rect)
    h_platforms_list = [H_Platform(0, HEIGHT-25, WIDTH, 50),H_Platform(50, 150, 100, 20), H_Platform(100, 350, 100, 20), H_Platform(250, 170, 100, 20), H_Platform(750, 180, 400, 20), H_Platform(950, 280, 450, 20), H_Platform(1250, 400, 190, 20), H_Platform(450, 450, 100, 20), H_Platform(500, 650, 350, 20), H_Platform(700, 540, 200, 20), H_Platform(1000, 450, 170, 20), H_Platform(1100, 900, 170, 20), H_Platform(890, 775, 140, 20)]
    v_platforms_list = [V_Platform(1900, 0, 20, 2 * HEIGHT - 50), V_Platform(0, 0, 20, 2 * HEIGHT - 50)]
    enemies_list = [Enemy(120, 270), Enemy(1300, 200),Enemy(1100,200), Enemy(575,570), Enemy(1300,320), Enemy(50,HEIGHT-110), Enemy(300,HEIGHT-110),Enemy(550,HEIGHT-110),Enemy(800,HEIGHT-110), Enemy(1050,HEIGHT-110), Enemy(1300, HEIGHT-110), Enemy(1550,HEIGHT-110), Enemy(1150, 820)]
    collectibles_list = [Collectible(280, 145), Collectible(150, 325), Collectible(770, 160 ), Collectible(1050, 260 ),Collectible(1150, 260), Collectible(500, 380), Collectible(600, 630), Collectible(900, 380), Collectible(1500, 280), Collectible(555, 40), Collectible(525, 200), Collectible(920,735), Collectible(1050, 425), Collectible(775,515), Collectible(1000, 160)]
    energies_list = [Energy(320, 145), Energy(1000, 260), Energy(550, 630)]

    #счёт игры
    font = pygame.font.Font(None, 36) # создание объекта, выбор размера шрифта
    score_text = font.render("Счёт: 0", True, SCORE_COLOR) # выбор цвета и текст
    score_rect = score_text.get_rect() # создание хитбокса текста
    score_rect.topleft = (WIDTH - 100, 20) # расположение хитбокса\текста на экране                

    #HP игрока
    font_hp = pygame.font.Font(None, 48) # создание объекта, выбор размера шрифта
    hp_text = font_hp.render("Здоровье: ", player.health, True, (255, 0, 0)) # выбор цвета и текст
    hp_rect = hp_text.get_rect()
    hp_rect.topleft = (0, 0)

    #Таймер игрока
    font_timer = pygame.font.Font(None, 60)
    timer_text =font_timer.render("Времени осталось: ", str(timer), True, (0, 0, 0))
    timer_rect = timer_text.get_rect()
    timer_rect.topleft = (WIDTH//2 - 300, 40)


    #создаем групп спрайтов
    player_and_platforms = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    collectibles = pygame.sprite.Group()
    energies = pygame.sprite.Group()

    #в четырех циклах добавляем объекты в соответствующие группы
    for i in enemies_list:
        enemies.add(i)

    for i in h_platforms_list:
        player_and_platforms.add(i)

    for i in v_platforms_list:
        player_and_platforms.add(i)

    for i in collectibles_list:
        collectibles.add(i)

    for i in energies_list:
        energies.add(i)

    #игровой цикл
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        #проверяем нажатие на клавиши для перемещения
        keys = pygame.key.get_pressed()
        player.x_velocity = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x_velocity = -player.speed
            player_img = pygame.transform.flip(player.image, True, False)
            #screen.blit(player.image, player.rect)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x_velocity = player.speed
            player_img = pygame.transform.flip(player.image, False, False)
        #условие прыжка более сложное
        if(keys[pygame.K_SPACE] or reload_energy > 0) and player.on_ground == True:
            player.y_velocity = -9
            player.on_ground = False

        #гравитация для игрока
        player.y_velocity += 0.3 

        #обновляем значения атрибутов игрока и врагов
        player.update()
        enemies.update()

        #отрисовываем фон, платформы, врагов и собираемые предметы
        screen.blit(bg_gameplay, (0, 0))
        screen.blit(player_img, player.rect)
        player_and_platforms.draw(screen)
        for enemy in enemies:
            screen.blit(enemy.image, enemy.rect)
        for collectible in collectibles:
            screen.blit(collectible.image, collectible.rect)
        for energy in energies:
            screen.blit(energy.image, energy.rect)
        if has_portal == True:
            screen.blit(portal.image, portal.rect)

        #проверяем все возможные коллизии
        check_h_collision_platforms(player, h_platforms_list)
        check_v_collision_platforms(player, v_platforms_list)
        check_collision_enemies(player, enemies_list)
        check_collision_collectibles(player, collectibles_list)
        check_collision_energies(player, energies_list, maxReload_energy)
        if has_portal == True:
            check_collision_portal(player, portal)

        #уменьшаем перезарядку если есть
        if(reload_energy > 0):
            reload_energy -= 1/60
        elif(reload_energy <= 0):
            player.speed = 5
            player.change_image(player_skin)

        if(player.cooldown > 0):
            player.cooldown -= 1/60

        if(timer > 0):
            timer -= 1/60 
        else:
            gameover()

        #обновление счёта на экране
        score_text = font.render("Счёт: " + str(score), True, SCORE_COLOR)
        hp_text = font_hp.render("Здоровье: " + str(player.health), True, (255, 0, 0))
        timer_text = font_timer.render("Времени осталось: " + str(int(timer)), True, (0, 0, 0))
        screen.blit(score_text, score_rect)
        screen.blit(hp_text, hp_rect)
        screen.blit(timer_text, timer_rect)
        
        #обновление экрана и установка частоты кадров
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

menu()