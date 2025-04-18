import pygame
import random
import psycopg2
username = input("Введите имя пользователя: ")

#база данных

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="maradato2512",
        port="5432"
    )

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users1 WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        print("Добро пожаловать,", username)
    else:
        cur.execute("INSERT INTO users1 (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print("Пользователь создан:", username)
    cur.close()
    conn.close()
    return user_id

def get_last_level(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT level FROM user_score1 WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else 1

def save_progress(user_id, level, score):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score1 (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()
    cur.close()
    conn.close()
    print("Прогресс сохранён!")

#игра

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 20)
def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))

def generate_food(snake, walls):
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

def generate_walls():
    walls = []
    for x in range(0, WIDTH, CELL_SIZE):
        walls.append((x, 0))
        walls.append((x, HEIGHT - CELL_SIZE))
    for y in range(0, HEIGHT, CELL_SIZE):
        walls.append((0, y))
        walls.append((WIDTH - CELL_SIZE, y))
    return walls

#вход пользователя

user_id = get_or_create_user(username)
level = get_last_level(user_id)
score = 0
speed = 10 + (level - 1) * 2

#игровой цикл

clock = pygame.time.Clock()
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)
walls = generate_walls()
food = generate_food(snake, walls)

running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 20):
        direction = (0, -20)
    elif keys[pygame.K_DOWN] and direction != (0, -20):
        direction = (0, 20)
    elif keys[pygame.K_LEFT] and direction != (20, 0):
        direction = (-20, 0)
    elif keys[pygame.K_RIGHT] and direction != (-20, 0):
        direction = (20, 0)
    elif keys[pygame.K_p]:
        save_progress(user_id, level, score)
        pygame.time.delay(500)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if (new_head in walls or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]):
        running = False

    if new_head == food:
        score += 1
        food = generate_food(snake, walls)
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    screen.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(screen, DARK_GREEN, (*wall, CELL_SIZE, CELL_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Level: {level}", 10, 30)
    pygame.display.flip()

pygame.quit()
