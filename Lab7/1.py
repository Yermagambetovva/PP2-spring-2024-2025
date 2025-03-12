#Create a simple clock application (only with minutes and seconds) 
#which is synchronized with system clock. 
#Use Mickey's right hand as minutes arrow and left - as seconds.

import pygame
from datetime import datetime

#инициализация pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

#загрузка изображения 
clock_face = pygame.image.load("mickeyclock.jpeg")
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))

#создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#функция для поворота изображения вокруг центра
def blit_rotate(surf, image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

#главный цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255)) #очистка экрана

    #получение текущего времени
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    #расчет углов поворота
    minute_angle = -(minutes * 6) #каждая минута - 6 градусов
    second_angle = -(seconds * 6) #каждая секунда - 6 градусов

    #отрисовка изображения два раза — по минутам и по секундам
    #но каждый раз очищаем экран, чтобы не было наложения
    blit_rotate(screen, clock_face, minute_angle, CENTER)  #минутная стрелка (правая рука)
    blit_rotate(screen, clock_face, second_angle, CENTER)  #секундная стрелка (левая рука)

    #обновление экрана
    pygame.display.flip()

    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #ограничение частоты кадров
    clock.tick(1)

pygame.quit()
