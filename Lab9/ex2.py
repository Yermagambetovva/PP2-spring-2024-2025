import pygame 
import random

pygame.init()

#настройки окна
WIDTH, HEIGHT = 600, 400                     #ширина и высота игрового окна
CELL_SIZE = 20                               #размер клетки (для сетки)
screen = pygame.display.set_mode((WIDTH, HEIGHT))   #создаём окно игры
pygame.display.set_caption("Snake Game")     #устанавливаем заголовок окна

#цвета
WHITE = (255, 255, 255)                      #белый цвет
GREEN = (0, 255, 0)                          #зелёный цвет для змеи
DARK_GREEN = (0, 155, 0)                     #тёмно-зелёный цвет для стен
RED = (255, 0, 0)                            #красный цвет для еды
BLACK = (0, 0, 0)                            #чёрный фон

#функция для отрисовки текста
font = pygame.font.SysFont("Arial", 20)      #шрифт Arial, размер 20
def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))   #рисуем текст на экране

#функция генерации еды в свободной клетке
def generate_food(snake, walls):
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE  #случайная координата X
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE #случайная координата Y
        if (x, y) not in snake and (x, y) not in walls:                      #проверка, чтобы еда не появилась на змее или стене
            weight = random.choice([1, 2, 3])                                #выбираем случайный вес еды
            timer = pygame.time.get_ticks()                                 #запоминаем время создания еды
            return (x, y), weight, timer                                    #возвращаем позицию, вес и время

#создание стен по краям экрана
def generate_walls():
    walls = []
    for x in range(0, WIDTH, CELL_SIZE):
        walls.append((x, 0))                         #верхняя граница
        walls.append((x, HEIGHT - CELL_SIZE))        #нижняя граница
    for y in range(0, HEIGHT, CELL_SIZE):
        walls.append((0, y))                         #левая граница
        walls.append((WIDTH - CELL_SIZE, y))         #правая граница
    return walls

clock = pygame.time.Clock()                          #таймер для контроля FPS

snake = [(100, 100), (80, 100), (60, 100)]            #начальная позиция змеи
direction = (20, 0)                                   #движение вправо
walls = generate_walls()                              #создаём стены
food_pos, food_weight, food_timer = generate_food(snake, walls)  #первая еда

score = 0                                             #начальный счёт
level = 1                                             #начальный уровень
speed = 10                                            #начальная скорость

FOOD_LIFETIME = 5000                                  #время жизни еды в миллисекундах

running = True
while running:
    clock.tick(speed)                                 #ограничиваем FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:                 #если нажали на крестик
            running = False

    #управление стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 20):        #вверх
        direction = (0, -20)
    elif keys[pygame.K_DOWN] and direction != (0, -20):   #вниз
        direction = (0, 20)
    elif keys[pygame.K_LEFT] and direction != (20, 0):    #влево
        direction = (-20, 0)
    elif keys[pygame.K_RIGHT] and direction != (-20, 0):  #вправо
        direction = (20, 0)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])  #новая голова змеи
    snake.insert(0, new_head)                                           #добавляем её в начало

    #проверка на столкновения
    if (new_head in walls or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]):
        running = False                                                 #конец игры при столкновении

    #проверка поедания еды
    if new_head == food_pos:
        score += food_weight                                            #добавляем вес еды к счёту
        if score % 3 == 0:                                              #каждые 3 очка — новый уровень
            level += 1
            speed += 2                                                 #увеличиваем скорость
        food_pos, food_weight, food_timer = generate_food(snake, walls) #создаём новую еду
    else:
        snake.pop()                                                    #если не еда — удаляем хвост

    #проверка таймера еды
    if pygame.time.get_ticks() - food_timer > FOOD_LIFETIME:           #если прошло больше FOOD_LIFETIME мс
        food_pos, food_weight, food_timer = generate_food(snake, walls) #обновляем еду

    #отрисовка экрана
    screen.fill(BLACK)                                                 #фон

    for wall in walls:
        pygame.draw.rect(screen, DARK_GREEN, (*wall, CELL_SIZE, CELL_SIZE)) #рисуем стены

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))   #рисуем змею

    pygame.draw.rect(screen, RED, (*food_pos, CELL_SIZE, CELL_SIZE))        #рисуем еду

    draw_text(f"Score: {score}", 10, 10)                                    #отображаем счёт
    draw_text(f"Level: {level}", 10, 30)                                    #отображаем уровень
    draw_text(f"Weight: {food_weight}", 10, 50)                             #отображаем вес еды
    time_left = max(0, (FOOD_LIFETIME - (pygame.time.get_ticks() - food_timer)) // 1000)
    draw_text(f"Time left: {time_left}s", 10, 70)                           #оставшееся время до исчезновения еды

    pygame.display.flip()                                                  #обновляем экран

pygame.quit()  #завершаем игру
