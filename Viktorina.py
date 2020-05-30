import pygame

get_width = 1366
get_height = 768
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
PALEVIOLETRED = (219, 112, 147)
ROYALBLUE = (65, 105, 225)
TOMATO = (165, 42, 42)
DARKBLUE = (65, 105, 225)
MINIBLUE = (183, 187, 240)
CVET = (230, 208, 170)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((get_width, get_height), pygame.FULLSCREEN)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.mixer.music.load('uku.mp3')
pygame.mixer.music.play()
pygame.mixer.music.play(loops=-1)
foon = pygame.image.load("wa.bmp")
foon_top = screen.get_height() - foon.get_height()
foon_left = screen.get_width() / 2 - foon.get_width() / 2
screen.blit(foon, (foon_left, foon_top))
count = 0
font = pygame.font.SysFont('comicsansms', 100)
text = font.render("Викторина", True, PALEVIOLETRED)
screen.blit(text, [450, 50])
button = pygame.Rect(610, 210, 200, 60)
pygame.draw.rect(screen, MINIBLUE, button)
font1 = pygame.font.SysFont('comicsansms', 50)
text1 = font1.render("Начать", True, PALEVIOLETRED)
screen.blit(text1, [630, 200])
button2 = pygame.Rect(1250, 50, 60, 60)
pygame.draw.rect(screen, CVET, button2)
font2 = pygame.font.SysFont('comicsansms', 50)
text2 = font2.render("x", True, PALEVIOLETRED)
screen.blit(text2, [1265, 40])

pygame.display.update()
pygame.display.flip()

count = 0


running = True


def fon():
    screen.fill(WHITE)
    ship1 = pygame.image.load("new.bmp")
    ship_top1 = screen.get_height() - ship1.get_height()
    ship_left1 = screen.get_width() / 2 - ship1.get_width() / 2
    screen.blit(ship1, (ship_left1, ship_top1))
    pygame.draw.rect(screen, [230, 208, 170], button2)
    text2 = font2.render("x", True, ROYALBLUE)
    screen.blit(text2, [1265, 40])


def vopros1(count):
    fon()
    vop1 = False
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
    pygame.draw.rect(screen, MINIBLUE, button3)
    text5 = font5.render("2) Дашур", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button4)
    text6 = font5.render("3) Пирамида Хеопса", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button5)
    text7 = font5.render("4) Пирамида Менкаура", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button3)
                    pygame.display.flip()
                    vopros2(count, vop1)
                if button4.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button4)
                    pygame.display.flip()
                    vopros2(count, vop1)
                if button5.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, DARKBLUE, button5)
                    pygame.display.flip()
                    vop1 = True
                    print(vop1)
                    count += 1
                    print(count)
                    vopros2(count, vop1)
                if button6.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button6)
                    pygame.display.flip()
                    vopros2(count, vop1)

        pygame.display.update()
        pygame.display.flip()

    return count, vop1

def vopros2(count, vop1):
    fon()
    vop2 = False
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
    pygame.draw.rect(screen, MINIBLUE, button3)
    text5 = font5.render("2) Рим", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button4)
    text6 = font5.render("3) Ханигальбат", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button5)
    text7 = font5.render("4) Мидия", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, DARKBLUE, button3)
                    pygame.display.flip()
                    vop2 = True
                    count = count + 1
                    print(count)
                    vopros3(count, vop1, vop2)
                if button4.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button4)
                    pygame.display.flip()
                    vopros3(count, vop1, vop2)
                if button5.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button5)
                    pygame.display.flip()
                    vopros3(count, vop1, vop2)
                if button6.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button6)
                    pygame.display.flip()
                    vopros3(count, vop1, vop2)

        pygame.display.update()
        pygame.display.flip()
    return count, vop1, vop2


def vopros3(count, vop1, vop2):
    fon()
    vop3 = False
    im1 = pygame.image.load("zevs.bmp")
    screen.blit(im1, [450, 80])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №3", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("В каком веке была воздвигнута статуя Зевса в Олимпии?", True, ROYALBLUE)
    screen.blit(text3, [400, 440])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) IV в. н.э.", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button3)
    text5 = font5.render("2) III в. д.н.э.", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button4)
    text6 = font5.render("3) I в. н.э.", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button5)
    text7 = font5.render("4) V в. д.н.э.", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button3)
                    pygame.display.flip()
                    vopros4(count, vop1, vop2, vop3)
                if button4.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button4)
                    pygame.display.flip()
                    vopros4(count, vop1, vop2, vop3)
                if button5.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button5)
                    pygame.display.flip()
                    vopros4(count, vop1, vop2, vop3)
                if button6.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, DARKBLUE, button6)
                    pygame.display.flip()
                    vop3 = True
                    count = count + 1
                    print(count)
                    vopros4(count, vop1, vop2, vop3)

        pygame.display.update()
        pygame.display.flip()
    return count, vop1, vop2, vop3


def vopros4(count, vop1, vop2, vop3):
    fon()
    vop4 = False
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
    pygame.draw.rect(screen, MINIBLUE, button3)
    text5 = font5.render("2) Херсифрон", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button4)
    text6 = font5.render("3) Марк Витрувий Поллион", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button5)
    text7 = font5.render("4) Страбон", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button3)
                    pygame.display.flip()
                    vopros5(count, vop1, vop2, vop3, vop4)
                if button4.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, DARKBLUE, button4)
                    pygame.display.flip()
                    vop4 = True
                    count = count + 1
                    print(count)
                    vopros5(count, vop1, vop2, vop3, vop4)
                if button5.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button5)
                    pygame.display.flip()
                    vopros5(count, vop1, vop2, vop3, vop4)
                if button6.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button6)
                    pygame.display.flip()
                    vopros5(count, vop1, vop2, vop3, vop4)

        pygame.display.update()
        pygame.display.flip()
    return count, vop1, vop2, vop3, vop4


def vopros5(count, vop1, vop2, vop3, vop4):
    fon()
    vop5 = False
    im1 = pygame.image.load("mavz.bmp")
    screen.blit(im1, [450, 90])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №5", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("Кем был разработан проект Мавзолей в Галикарнасе?", True, ROYALBLUE)
    screen.blit(text3, [400, 450])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) Калликрат", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button3)
    text5 = font5.render("2) Фидий и Поликлет", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button4)
    text6 = font5.render("3) Перикл", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button5)
    text7 = font5.render("4) Пифей", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button3)
                    pygame.display.flip()
                    vopros6(count, vop1, vop2, vop3, vop4, vop5)
                if button4.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button4)
                    pygame.display.flip()
                    vopros6(count, vop1, vop2, vop3, vop4, vop5)
                if button5.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button5)
                    pygame.display.flip()
                    vopros6(count, vop1, vop2, vop3, vop4, vop5)
                if button6.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, DARKBLUE, button6)
                    pygame.display.flip()
                    vop5 = True
                    count = count + 1
                    print(count)
                    vopros6(count, vop1, vop2, vop3, vop4, vop5)

        pygame.display.update()
        pygame.display.flip()
    return count, vop1, vop2, vop3, vop4, vop5


def vopros6(count, vop1, vop2, vop3, vop4, vop5):
    fon()
    vop6 = False
    im1 = pygame.image.load("kolos.bmp")
    screen.blit(im1, [450, 90])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №6", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("Какова причина разрушения Колосса Родосского?", True, ROYALBLUE)
    screen.blit(text3, [450, 430])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) Ураган", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button3)
    text5 = font5.render("2) Землетрясение", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button4)
    text6 = font5.render("3) Ледниковый период", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button5)
    text7 = font5.render("4) Принудительное разрушение", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button3)
                    pygame.display.flip()
                    vopros7(count, vop1, vop2, vop3, vop4, vop5, vop6)
                if button4.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, DARKBLUE, button4)
                    pygame.display.flip()
                    count = count + 1
                    vop6 = True
                    print(count)
                    vopros7(count, vop1, vop2, vop3, vop4, vop5, vop6)
                if button5.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button5)
                    pygame.display.flip()
                    vopros7(count, vop1, vop2, vop3, vop4, vop5, vop6)
                if button6.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button6)
                    pygame.display.flip()
                    vopros7(count, vop1, vop2, vop3, vop4, vop5, vop6)

        pygame.display.update()
        pygame.display.flip()
    return count, vop1, vop2, vop3, vop4, vop5, vop6


def vopros7(count, vop1, vop2, vop3, vop4, vop5, vop6):
    fon()
    vop7 = False
    im1 = pygame.image.load("mayak.bmp")
    screen.blit(im1, [360, 90])
    font3 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Вопрос №7", True, ROYALBLUE)
    screen.blit(text, [450, 20])
    font4 = pygame.font.SysFont('comicsansms', 25)
    text3 = font4.render("Для чего предназначался Александрийский маяк?", True, ROYALBLUE)
    screen.blit(text3, [450, 430])
    font5 = pygame.font.SysFont('comicsansms', 30)
    text4 = font5.render("1) Для судоходства", True, ROYALBLUE)
    screen.blit(text4, [540, 490])
    button3 = pygame.Rect(490, 495, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button3)
    text5 = font5.render("2) Для смотровой площадки", True, ROYALBLUE)
    screen.blit(text5, [540, 540])
    button4 = pygame.Rect(490, 545, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button4)
    text6 = font5.render("3) Для хранения овощей", True, ROYALBLUE)
    screen.blit(text6, [540, 590])
    button5 = pygame.Rect(490, 595, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button5)
    text7 = font5.render("4) Для красоты", True, ROYALBLUE)
    screen.blit(text7, [540, 640])
    button6 = pygame.Rect(490, 645, 40, 40)
    pygame.draw.rect(screen, MINIBLUE, button6)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button3.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, DARKBLUE, button3)
                    pygame.display.flip()
                    vop7 = True
                    count = count + 1
                    print(count)
                    finish(count, vop1, vop2, vop3, vop4, vop5, vop6, vop7)
                if button4.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button4)
                    pygame.display.flip()
                    finish(count, vop1, vop2, vop3, vop4, vop5, vop6, vop7)
                if button5.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button5)
                    pygame.display.flip()
                    finish(count, vop1, vop2, vop3, vop4, vop5, vop6, vop7)
                if button6.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, TOMATO, button6)
                    pygame.display.flip()
                    finish(count, vop1, vop2, vop3, vop4, vop5, vop6, vop7)

        pygame.display.update()
        pygame.display.flip()
    return count, vop1, vop2, vop3, vop4, vop5, vop6, vop7


def finish(count, vop1, vop2, vop3, vop4, vop5, vop6, vop7):
    print(vop1)
    fon()
    font3 = pygame.font.SysFont('comicsansms', 50)
    font5 = pygame.font.SysFont('comicsansms', 50)
    text = font3.render("Количество очков:", True, ROYALBLUE)
    text2 = font5.render(str(count), True, ROYALBLUE)
    screen.blit(text, [450, 50])
    screen.blit(text2, [660, 150])
    button = pygame.Rect(570, 465, 220, 60)
    pygame.draw.rect(screen, MINIBLUE, button)
    font1 = pygame.font.SysFont('comicsansms', 40)
    text1 = font1.render("Подробнее", True, ROYALBLUE)
    screen.blit(text1, [570, 460])
    button3 = pygame.Rect(475, 540, 420, 60)
    pygame.draw.rect(screen, MINIBLUE, button3)
    font3 = pygame.font.SysFont('comicsansms', 40)
    text3 = font3.render("Попробовать ещё раз", True, ROYALBLUE)
    screen.blit(text3, [475, 535])
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
                if button.collidepoint(mouse_pos):
                    print(count)
                    info(vop1,vop2, vop3, vop4, vop5, vop6, vop7)
                if button3.collidepoint(mouse_pos):
                    count = 0
                    vopros1(count)

        pygame.display.update()
        pygame.display.flip()
    return count, vop1, vop2, vop3, vop4, vop5, vop6, vop7


def info(vop1,vop2, vop3, vop4, vop5, vop6, vop7):
    font1 = pygame.font.SysFont('comicsansms', 25)
    if not vop1:
        text1 = font1.render("1.Вы ответили неправильно, правильный ответ: Пирамида Хеопса", True, TOMATO)
        screen.blit(text1, [20, 220])
        info2(vop2, vop3, vop4, vop5, vop6, vop7)
    else:
        text1 = font1.render("1.Вы ответили правильно", True, DARKBLUE)
        screen.blit(text1, [20, 220])
        info2(vop2, vop3, vop4, vop5, vop6, vop7)


def info2(vop2, vop3, vop4, vop5, vop6, vop7):
    font1 = pygame.font.SysFont('comicsansms', 25)

    if not vop2:
        text1 = font1.render("2.Вы ответили неправильно, правильный ответ: Вавилон", True, TOMATO)
        screen.blit(text1, [20, 250])
        info3(vop3, vop4, vop5, vop6, vop7)
    else:
        text1 = font1.render("2.Вы ответили правильно", True, DARKBLUE)
        screen.blit(text1, [20, 250])
        info3(vop3, vop4, vop5, vop6, vop7)


def info3(vop3, vop4, vop5, vop6, vop7):
    font1 = pygame.font.SysFont('comicsansms', 25)

    if not vop3:
        text1 = font1.render("3.Вы ответили неправильно, правильный ответ: V в. д.н.э.", True, TOMATO)
        screen.blit(text1, [20, 280])
        info4(vop4, vop5, vop6, vop7)
    else:
        text1 = font1.render("3.Вы ответили правильно", True, DARKBLUE)
        screen.blit(text1, [20, 280])
        info4(vop4, vop5, vop6, vop7)


def info4(vop4, vop5, vop6, vop7):
    font1 = pygame.font.SysFont('comicsansms', 25)

    if not vop4:
        text1 = font1.render("4.Вы ответили неправильно, правильный ответ: Херсифрон", True, TOMATO)
        screen.blit(text1, [20, 310])
        info5(vop5, vop6, vop7)
    else:
        text1 = font1.render("4.Вы ответили правильно", True, DARKBLUE)
        screen.blit(text1, [20, 310])
        info5(vop5, vop6, vop7)


def info5(vop5, vop6, vop7):
    font1 = pygame.font.SysFont('comicsansms', 25)

    if not vop5:
        text1 = font1.render("5.Вы ответили неправильно, правильный ответ: Пифей", True, TOMATO)
        screen.blit(text1, [20, 340])
        info6(vop6,vop7)
    else:
        text1 = font1.render("5.Вы ответили правильно", True, DARKBLUE)
        screen.blit(text1, [20, 340])
        info6(vop6,vop7)


def info6(vop6, vop7):
    font1 = pygame.font.SysFont('comicsansms', 25)

    if not vop6:
        text1 = font1.render("6.Вы ответили неправильно, правильный ответ: Землетрясение", True, TOMATO)
        screen.blit(text1, [20, 370])
        info7(vop7)
    else:
        text1 = font1.render("6.Вы ответили правильно", True, DARKBLUE)
        screen.blit(text1, [20, 370])
        info7(vop7)


def info7(vop7):
    font1 = pygame.font.SysFont('comicsansms', 25)
    if not vop7:
        text1 = font1.render("7.Вы ответили неправильно, правильный ответ: Для судоходства", True, TOMATO)
        screen.blit(text1, [20, 400])
    else:
        text1 = font1.render("7.Вы ответили правильно", True, DARKBLUE)
        screen.blit(text1, [20, 400])


if __name__ == '__main__':
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        pygame.mixer.music.get_busy()
        # Ввод процесса (события)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button.collidepoint(mouse_pos):
                    vopros1(count)
                if button2.collidepoint(mouse_pos):
                    pygame.quit()

        pygame.display.update()
        pygame.display.flip()
pygame.quit()
