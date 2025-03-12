import pygame

#инициализация pygame и микшера
pygame.init()
pygame.mixer.init()

#список треков 
playlist = ["track1.mp3", "track2.mp3"]
current = 0

#функция воспроизведения трека
def play(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    print("Playing:", playlist[index])

#создание простого окна
screen = pygame.display.set_mode((400, 100))

running = True
play(current)  #сразу запускаем первый трек

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #клавиатурное управление
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  #Play / Resume
                pygame.mixer.music.unpause()
                print("Resumed")
            elif event.key == pygame.K_s:  #Stop
                pygame.mixer.music.stop()
                print("Stopped")
            elif event.key == pygame.K_n:  #Next
                current = (current + 1) % len(playlist)
                play(current)
            elif event.key == pygame.K_b:  #Previous
                current = (current - 1) % len(playlist)
                play(current)
            elif event.key == pygame.K_SPACE:  #Pause
                pygame.mixer.music.pause()
                print("Paused")

pygame.quit()
