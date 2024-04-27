
def init_but(screen, buttons):
    for button in buttons:
        screen.blit(button.image, button.rect)