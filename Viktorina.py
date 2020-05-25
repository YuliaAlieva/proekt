import pygame
import random
import easygui

WIDTH = 1080
HEIGHT = 1080
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
FUCHSIA = (255, 0, 255)
PALEVIOLETRED = (219, 112, 147)
TURQUOISE = (64, 224, 208)
ORCHID = (218, 112, 214)
ROYALBLUE = (65, 105, 225)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.mixer.music.load('uku.mp3')
pygame.mixer.music.play()
rect = pygame.Rect(40, 40, 120, 120)
color = (255, 255, 255)
ship = pygame.image.load("wa.bmp")
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width() / 2 - ship.get_width() / 2
screen.blit(ship, (ship_left, ship_top))
count = 0
font = pygame.font.SysFont('comicsansms', 100)
text = font.render("Викторина", True, PALEVIOLETRED)
screen.blit(text, [450, 50])
button = pygame.Rect(610, 210, 200, 60)
pygame.draw.rect(screen, [183, 187, 240], button)
font1 = pygame.font.SysFont('comicsansms', 50)
text1 = font1.render("Начать", True, PALEVIOLETRED)
screen.blit(text1, [630, 200])
button2 = pygame.Rect(1250, 50, 60, 60)
pygame.draw.rect(screen, [230, 208, 170], button2)
font2 = pygame.font.SysFont('comicsansms', 50)
text2 = font2.render("x", True, PALEVIOLETRED)
screen.blit(text2, [1265, 40])

pygame.display.update()

pygame.display.flip()


# Цикл игры
def main():
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        pygame.mixer.music.get_busy()

        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
            # screen.fill(WHITE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button.collidepoint(mouse_pos):
                    vopros1()
                    # screen.fill(WHITE)
                    print('button was pressed at {0}'.format(mouse_pos))
                if button2.collidepoint(mouse_pos):
                    pygame.quit()

        # screen.fill(WHITE)

        pygame.display.update()

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()


def fon():
    screen.fill(WHITE)
    global count
    # pygame.display.update()
    ship1 = pygame.image.load("new.bmp")
    ship_top1 = screen.get_height() - ship1.get_height()
    ship_left1 = screen.get_width() / 2 - ship1.get_width() / 2
    screen.blit(ship1, (ship_left1, ship_top1))
    pygame.draw.rect(screen, [230, 208, 170], button2)
    text2 = font2.render("x", True, ROYALBLUE)
    screen.blit(text2, [1265, 40])


def vopros1():
    fon()
    global count
    im1 = pygame.image.load("heops.bmp")
    screen.blit(im1, [450, 80])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №1", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("Cамое древнее, первое чудо света и единственное, "
                         "сохранившееся до наших дней.", True, ROYALBLUE)
    screen.blit(text3, [230, 450])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) Пирамида Херфена", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button3)
    text5 = font5.render("2) Дашур", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button4)
    text6 = font5.render("3) Пирамида Хеопса", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button5)
    text7 = font5.render("4) Пирамида Менкаура", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    screen.fill(WHITE)
                    vopros2()

                if button4.collidepoint(mouse_pos):
                    vopros2()

                if button5.collidepoint(mouse_pos):
                    # global count
                    count += 1
                    print(count)
                    vopros2()
                if button6.collidepoint(mouse_pos):
                    vopros2()

        pygame.display.update()
        pygame.display.flip()


def vopros2():
    fon()
    global count
    im1 = pygame.image.load("sady.bmp")
    screen.blit(im1, [450, 120])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №2", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("Где располагались Висячие сады Семирамиды?", True, ROYALBLUE)
    screen.blit(text3, [400, 420])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) Вавилон", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button3)
    text5 = font5.render("2) Рим", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button4)
    text6 = font5.render("3) Ханигальбат", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button5)
    text7 = font5.render("4) Мидия", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    count = count + 1
                    print(count)
                    vopros3()
                if button4.collidepoint(mouse_pos):
                    vopros3()
                if button5.collidepoint(mouse_pos):
                    # count = count + 1
                    vopros3()
                    # print(count)
                if button6.collidepoint(mouse_pos):
                    vopros3()

        pygame.display.update()
        pygame.display.flip()


def vopros3():
    fon()
    global count
    im1 = pygame.image.load("zevs.bmp")
    screen.blit(im1, [450, 80])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №3", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("В каком веке была воздвигнута статуя Зевса в Олимпии??", True, ROYALBLUE)
    screen.blit(text3, [400, 440])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) IV в. н.э.", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button3)
    text5 = font5.render("2) III в. д.н.э.", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button4)
    text6 = font5.render("3) I в. н.э.", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button5)
    text7 = font5.render("4) V в. д.н.э.", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    vopros4()
                if button4.collidepoint(mouse_pos):
                    vopros4()
                if button5.collidepoint(mouse_pos):
                    # count = count + 1
                    vopros4()
                    # print(count)
                if button6.collidepoint(mouse_pos):
                    count = count + 1
                    print(count)
                    vopros4()
                    # screen.fill(WHITE)

        pygame.display.update()
        pygame.display.flip()


def vopros4():
    fon()
    global count
    im1 = pygame.image.load("hram.bmp")
    screen.blit(im1, [400, 90])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №4", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("Архитектор Храма Артемиды Эфесской", True, ROYALBLUE)
    screen.blit(text3, [400, 450])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) Плиний", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button3)
    text5 = font5.render("2) Херсифрон", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button4)
    text6 = font5.render("3) Марк Витрувий Поллион", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button5)
    text7 = font5.render("4) Страбон", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, [183, 187, 240], button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    vopros3()
                if button4.collidepoint(mouse_pos):
                    count = count + 1
                    print(count)

                if button5.collidepoint(mouse_pos):
                    vopros3()
                if button6.collidepoint(mouse_pos):
                    vopros3()

        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
pygame.quit()
