#Тут в будущем будет много методов для инициализации разных классов
#Инициализация кнопок
def init_but(screen, buttons):
    for button in buttons: #Выбираем каждую из списка
        screen.blit(button.image, button.rect)  #Инициализируем на экране