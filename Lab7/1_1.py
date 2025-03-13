import pygame
from datetime import datetime

#инициализация Pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

#создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#загрузка изображений
clock_face = pygame.image.load("mickeyclock.jpeg")
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))

right_hand = pygame.image.load("min_hand.png").convert_alpha()
left_hand = pygame.image.load("sec_hand.png").convert_alpha()

#установка начальных точек поворота (настраиваем при необходимости)
right_hand_origin = right_hand.get_rect().center
left_hand_origin = left_hand.get_rect().center

#функция поворота изображения вокруг центра
def blit_rotate(surf, image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pivot)
    surf.blit(rotated_image, new_rect.topleft)

#главный цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))

    #отображаем фон
    screen.blit(clock_face, (0, 0))

    #получаем текущее время
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    #углы поворота
    minute_angle = -(minutes * 6)  # 360/60
    second_angle = -(seconds * 6)

    #отображаем стрелки
    blit_rotate(screen, right_hand, minute_angle, CENTER)  #минутная стрелка (правая рука)
    blit_rotate(screen, left_hand, second_angle, CENTER)   #секундная стрелка (левая рука)

    #обновление экрана
    pygame.display.flip()

    #проверка на выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #обновление каждую секунду
    clock.tick(1)

pygame.quit()
