import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#настройка кадров в секунду и таймера
FPS = 60
FramePerSec = pygame.time.Clock()
 
#определение цветов в формате RGB
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#размеры экрана и начальные параметры игры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  #счётчик собранных монет

#инициализация шрифтов и надписи "Game Over"
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#загрузка фонового изображения
background = pygame.image.load("AnimatedStreet.png")

#создание основного игрового окна
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#класс врага, который двигается сверху вниз и увеличивает счёт при выходе за экран
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#класс игрока, которым можно управлять с помощью клавиш влево и вправо
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

#класс монеты, которая появляется в случайном месте и движется вниз
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(original_image, (32, 32))  # уменьшаем до нужного размера
        self.rect = self.image.get_rect()
        self.reset_position()

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        #перемещает монету в случайное положение в верхней части экрана
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -40))


#создание игрока, врага и монеты
P1 = Player()
E1 = Enemy()
C1 = Coin()

#создание групп спрайтов для удобного управления
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#настройка события, которое будет повышать скорость каждую секунду
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     #каждую секунду увеличиваем скорость движения
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #отображение фонового изображения
    DISPLAYSURF.blit(background, (0, 0))

    #отрисовка счёта и количества монет в верхней части экрана
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    #движение и отображение всех объектов на экране
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    #проверка столкновения игрока с монетой
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1       #увеличиваем счётчик монет
        C1.reset_position()  #перемещаем монету в новую случайную позицию

    #обновление экрана и установка FPS
    pygame.display.update()
    FramePerSec.tick(FPS)
