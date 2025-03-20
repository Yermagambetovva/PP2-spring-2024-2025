import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Рисовалка")
    clock = pygame.time.Clock()

    radius = 10
    color = (0, 0, 255)
    mode = 'draw'

    drawing = False
    points = []
    start_pos = None
    font = pygame.font.SysFont(None, 24)

    base_layer = pygame.Surface(screen.get_size())
    base_layer.fill((0, 0, 0))

    def draw_ui():
        texts = [
            "Режимы: [d] линия | [r] прямоугольник | [c] круг | [e] ластик",
            "Цвета: [1] красный | [2] зелёный | [3] синий | [4] белый (ластик)",
            f"Текущий режим: {mode} | Цвет: {color} | Размер кисти: {radius}"
        ]
        y = 5
        for t in texts:
            text_surface = font.render(t, True, (255, 255, 255))
            screen.blit(text_surface, (5, y))
            y += 25

    running = True
    while running:
        screen.blit(base_layer, (0, 0))
        draw_ui()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_r:
                    mode = 'rect'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_e:
                    mode = 'erase'

                elif event.key == pygame.K_1:
                    color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)
                elif event.key == pygame.K_4:
                    color = (255, 255, 255)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if mode == 'draw' or mode == 'erase':
                        points = [event.pos]
                elif event.button == 3:
                    radius = max(1, radius - 1)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    if mode == 'rect':
                        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                        pygame.draw.rect(base_layer, color, rect)
                    elif mode == 'circle':
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        radius_circle = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                        pygame.draw.circle(base_layer, color, center, radius_circle)
                    drawing = False
                    points = []

            elif event.type == pygame.MOUSEMOTION and drawing:
                pos = event.pos
                if mode == 'draw' or mode == 'erase':
                    points.append(pos)
                    if len(points) > 1:
                        pygame.draw.line(
                            base_layer,
                            color if mode == 'draw' else (0, 0, 0),
                            points[-2],
                            points[-1],
                            radius
                        )

        clock.tick(60)

    pygame.quit()

main()
