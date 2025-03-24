import pygame
import random

pygame.init()

#настройки окна
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

#цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#функция для отрисовки текста
font = pygame.font.SysFont("Arial", 20)
def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))

#функция для генерации еды в свободной клетке
def generate_food(snake, walls):
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

#создание стен (можно настроить по желанию)
def generate_walls():
    walls = []
    for x in range(0, WIDTH, CELL_SIZE):
        walls.append((x, 0))
        walls.append((x, HEIGHT - CELL_SIZE))
    for y in range(0, HEIGHT, CELL_SIZE):
        walls.append((0, y))
        walls.append((WIDTH - CELL_SIZE, y))
    return walls

clock = pygame.time.Clock()

snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)  #движение вправо
walls = generate_walls()
food = generate_food(snake, walls)

score = 0
level = 1
speed = 10  #начальная скорость

running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 20):
        direction = (0, -20)
    elif keys[pygame.K_DOWN] and direction != (0, -20):
        direction = (0, 20)
    elif keys[pygame.K_LEFT] and direction != (20, 0):
        direction = (-20, 0)
    elif keys[pygame.K_RIGHT] and direction != (-20, 0):
        direction = (20, 0)

    #движение змеи
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    #проверка на столкновение со стеной или выход за границу
    if (new_head in walls or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]):
        running = False

    #поедание еды
    if new_head == food:
        score += 1
        food = generate_food(snake, walls)
        if score % 3 == 0:
            level += 1
            speed += 2  #увеличение скорости
    else:
        snake.pop()

    #отрисовка
    screen.fill(BLACK)

    #стены
    for wall in walls:
        pygame.draw.rect(screen, DARK_GREEN, (*wall, CELL_SIZE, CELL_SIZE))

    #змея
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    #еда
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    #счёт и уровень
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Level: {level}", 10, 30)

    pygame.display.flip()

pygame.quit()
