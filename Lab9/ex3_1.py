import pygame                             #импортируем библиотеку pygame для создания графического окна
import math                               #импортируем math для работы с тригонометрией (например, для треугольника)

def main():
    pygame.init()                         #инициализируем все модули pygame
    screen = pygame.display.set_mode((640, 480))  #создаём окно 640x480 пикселей
    pygame.display.set_caption("Paint with Shapes")  #устанавливаем заголовок окна
    clock = pygame.time.Clock()          #создаём объект таймера для контроля FPS

    radius = 15                          #начальный радиус кисти для рисования
    mode = 'blue'                        #цвет по умолчанию — синий
    draw_mode = 'free'                   #режим рисования — свободный (кисть)
    points = []                          #список точек для свободного рисования
    shape_start = None                   #начальная точка для рисования фигуры
    drawing = False                      #флаг, указывает рисуется ли фигура

    buffer = screen.copy()              #буферное изображение, где храним уже нарисованные элементы

    while True:                         #основной игровой цикл
        pressed = pygame.key.get_pressed()  #получаем список всех нажатых клавиш

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]     #проверка нажатия Alt
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]  #проверка нажатия Ctrl

        for event in pygame.event.get():        #обрабатываем события
            if event.type == pygame.QUIT:       #если нажали крестик
                return
            if event.type == pygame.KEYDOWN:    #если нажали клавишу
                if event.key == pygame.K_w and ctrl_held:  #если Ctrl + W
                    return
                if event.key == pygame.K_F4 and alt_held:  #если Alt + F4
                    return
                if event.key == pygame.K_ESCAPE:           #если Escape
                    return

                if event.key == pygame.K_r:     #переключение цвета на красный
                    mode = 'red'
                elif event.key == pygame.K_g:   #зелёный
                    mode = 'green'
                elif event.key == pygame.K_b:   #синий
                    mode = 'blue'

                if event.key == pygame.K_1:     #режим квадрата
                    draw_mode = 'square'
                elif event.key == pygame.K_2:   #режим прямоугольного треугольника
                    draw_mode = 'right_triangle'
                elif event.key == pygame.K_3:   #режим равностороннего треугольника
                    draw_mode = 'equilateral_triangle'
                elif event.key == pygame.K_4:   #режим ромба
                    draw_mode = 'rhombus'
                elif event.key == pygame.K_f:   #свободное рисование (кисть)
                    draw_mode = 'free'
                elif event.key == pygame.K_c:   #очистка экрана
                    buffer.fill((0, 0, 0))      #заливаем буфер чёрным
                    points.clear()              #очищаем список точек
                elif event.key == pygame.K_s:
                    pygame.image.save(buffer, "paint.png") 

            if event.type == pygame.MOUSEBUTTONDOWN:     #нажатие кнопки мыши
                if event.button == 1:                    #левая кнопка мыши
                    if draw_mode == 'free':              #если режим кисти
                        radius = min(200, radius + 1)    #увеличиваем толщину кисти
                    else:
                        shape_start = event.pos          #запоминаем начальную точку для фигуры
                        drawing = True                   #включаем режим рисования фигуры
                elif event.button == 3:                  #правая кнопка мыши
                    radius = max(1, radius - 1)          #уменьшаем толщину кисти

            if event.type == pygame.MOUSEBUTTONUP:       #отпустили кнопку мыши
                if draw_mode != 'free' and drawing:      #если фигура и была начальная точка
                    shape_end = event.pos                #получаем конечную точку
                    draw_shape(buffer, shape_start, shape_end, draw_mode, mode)  #рисуем фигуру на буфере
                    shape_start = None                   #сбрасываем начальную точку
                    drawing = False                      #отключаем флаг рисования

            if event.type == pygame.MOUSEMOTION:         #движение мыши
                if draw_mode == 'free' and pygame.mouse.get_pressed()[0]:  #если нажата левая кнопка
                    position = event.pos                 #получаем текущую позицию
                    points.append(position)              #добавляем точку в список
                    points = points[-256:]               #ограничиваем до последних 256 точек
                    if len(points) >= 2:                 #если есть хотя бы 2 точки
                        drawLineBetween(buffer, len(points), points[-2], points[-1], radius, mode)  #рисуем линию

        screen.blit(buffer, (0, 0))                       #рисуем на экране всё, что есть в буфере

        if draw_mode != 'free' and drawing and shape_start:   #если рисуем фигуру в реальном времени
            current_pos = pygame.mouse.get_pos()              #получаем текущую позицию мыши
            preview_surface = buffer.copy()                   #копируем буфер для предварительного просмотра
            draw_shape(preview_surface, shape_start, current_pos, draw_mode, mode)  #рисуем фигуру
            screen.blit(preview_surface, (0, 0))              #отображаем поверх основного

        pygame.display.flip()                                 #обновляем окно
        clock.tick(60)                                        #ограничиваем до 60 кадров в секунду

#функция рисования плавной линии между двумя точками
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))              #градиент цветовой компоненты
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))                 #выбираем максимальное расстояние как число шагов

    for i in range(iterations):
        progress = i / iterations                      #доля пройденного пути
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])  #интерполяция координаты X
        y = int(aprogress * start[1] + progress * end[1])  #интерполяция координаты Y
        pygame.draw.circle(screen, color, (x, y), width)   #рисуем точку линии

#функция рисования фигур между двумя точками
def draw_shape(surface, start, end, shape, color_mode):
    color = (255, 255, 255) if color_mode == 'blue' else (255, 0, 0) if color_mode == 'red' else (0, 255, 0)  #выбираем цвет

    x1, y1 = start
    x2, y2 = end

    if shape == 'square':
        size = min(abs(x2 - x1), abs(y2 - y1))                 #выбираем минимальную сторону
        rect = pygame.Rect(x1, y1, size, size)                 #создаём прямоугольник
        pygame.draw.rect(surface, color, rect)                #рисуем квадрат

    elif shape == 'right_triangle':
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)])  #рисуем прямоугольный треугольник

    elif shape == 'equilateral_triangle':
        side = min(abs(x2 - x1), abs(y2 - y1))                 #длина стороны
        height = int((math.sqrt(3) / 2) * side)                #высота треугольника
        top = (x1 + side // 2, y1)                             #верхняя вершина
        left = (x1, y1 + height)                               #левая нижняя вершина
        right = (x1 + side, y1 + height)                       #правая нижняя вершина
        pygame.draw.polygon(surface, color, [top, left, right])  #рисуем треугольник

    elif shape == 'rhombus':
        dx = (x2 - x1) // 2
        dy = (y2 - y1) // 2
        center = (x1 + dx, y1 + dy)                            #центр ромба
        points = [
            (center[0], y1),                                   #верхняя вершина
            (x2, center[1]),                                   #правая вершина
            (center[0], y2),                                   #нижняя вершина
            (x1, center[1])                                    #левая вершина
        ]
        pygame.draw.polygon(surface, color, points)            #рисуем ромб

main()  #запускаем основную функцию
