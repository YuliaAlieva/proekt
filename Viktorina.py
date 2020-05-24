import pygame
import random

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
                    voprosy()
                    # screen.fill(WHITE)
                    print('button was pressed at {0}'.format(mouse_pos))
                if button2.collidepoint(mouse_pos):
                    pygame.quit()

        # screen.fill(WHITE)

        pygame.display.update()

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()


def voprosy():
    screen.fill(WHITE)
    # pygame.display.update()
    ship1 = pygame.image.load("new.bmp")
    ship_top1 = screen.get_height() - ship1.get_height()
    ship_left1 = screen.get_width() / 2 - ship1.get_width() / 2
    screen.blit(ship1, (ship_left1, ship_top1))
    im1 = pygame.image.load("heops.bmp")
    screen.blit(im1, [450, 80])
    pygame.draw.rect(screen, [230, 208, 170], button2)
    text2 = font2.render("x", True, ROYALBLUE)
    screen.blit(text2, [1265, 40])
    font = pygame.font.SysFont('comicsansms', 50)
    text = font.render("Вопрос №1", True, ROYALBLUE)
    screen.blit(text, [450, 20])


if __name__ == '__main__':
    main()
pygame.quit()