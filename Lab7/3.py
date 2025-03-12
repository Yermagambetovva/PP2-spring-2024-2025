import pygame  #для доступа к фреймворку PyGame

pygame.init()   #инициализирует все модули необходимые в PyGame

white = (255, 255, 255)
red = (255, 0, 0)
radius = 25
step = 20

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))  #запускаем окно нужного размера

#устанавливаем начальную позицию мяча в центр экрана
x = screen_width // 2
y = screen_height // 2

running = True   #пока выполняется основной цикл игры
clock = pygame.time.Clock()   #для того чтобы контролировать скорость игры

while running:
    clock.tick(60)  #ограничиваем количество кадров в секунду до 60 кадров в секунду

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #если закроет вкладку, игра останавливается 
            running = False

    #получаем список нажатых клавиш
    keys = pygame.key.get_pressed()

    #двигаем мяч, если клавиша нажата и не выходит за границы
    if keys[pygame.K_UP] and y - radius - step >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y + radius + step <= screen_height:
        y += step
    if keys[pygame.K_LEFT] and x - radius - step >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + radius + step <= screen_width:
        x += step

    #заливаем фон
    screen.fill(white)

    #рисуем мяч
    pygame.draw.circle(screen, red, (x, y), radius)

    #обновляем экран
    pygame.display.flip()  #для того, чтобы любые обновления, которые вы вносите на игровой экран, становились видимыми

pygame.quit()  #запускается при нажатии на кнопку "Закрыть" в углу окна
