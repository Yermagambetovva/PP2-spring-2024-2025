import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint with Shapes")
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    draw_mode = 'free'
    points = []
    shape_start = None
    drawing = False

    buffer = screen.copy()  #создаём буфер для хранения нарисованного

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                if event.key == pygame.K_1:
                    draw_mode = 'square'
                elif event.key == pygame.K_2:
                    draw_mode = 'right_triangle'
                elif event.key == pygame.K_3:
                    draw_mode = 'equilateral_triangle'
                elif event.key == pygame.K_4:
                    draw_mode = 'rhombus'
                elif event.key == pygame.K_f:
                    draw_mode = 'free'
                elif event.key == pygame.K_c:
                    buffer.fill((0, 0, 0))     #очистка экрана
                    points.clear()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if draw_mode == 'free':
                        radius = min(200, radius + 1)
                    else:
                        shape_start = event.pos
                        drawing = True
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if draw_mode != 'free' and drawing:
                    shape_end = event.pos
                    draw_shape(buffer, shape_start, shape_end, draw_mode, mode)
                    shape_start = None
                    drawing = False

            if event.type == pygame.MOUSEMOTION:
                if draw_mode == 'free' and pygame.mouse.get_pressed()[0]:
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
                    if len(points) >= 2:
                        drawLineBetween(buffer, len(points), points[-2], points[-1], radius, mode)

        screen.blit(buffer, (0, 0))  #перерисовываем сохранённое

        if draw_mode != 'free' and drawing and shape_start:
            current_pos = pygame.mouse.get_pos()
            preview_surface = buffer.copy()
            draw_shape(preview_surface, shape_start, current_pos, draw_mode, mode)
            screen.blit(preview_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def draw_shape(surface, start, end, shape, color_mode):
    color = (255, 255, 255) if color_mode == 'blue' else (255, 0, 0) if color_mode == 'red' else (0, 255, 0)

    x1, y1 = start
    x2, y2 = end

    if shape == 'square':
        size = min(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, size, size)
        pygame.draw.rect(surface, color, rect)

    elif shape == 'right_triangle':
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)])

    elif shape == 'equilateral_triangle':
        side = min(abs(x2 - x1), abs(y2 - y1))
        height = int((math.sqrt(3) / 2) * side)
        top = (x1 + side // 2, y1)
        left = (x1, y1 + height)
        right = (x1 + side, y1 + height)
        pygame.draw.polygon(surface, color, [top, left, right])

    elif shape == 'rhombus':
        dx = (x2 - x1) // 2
        dy = (y2 - y1) // 2
        center = (x1 + dx, y1 + dy)
        points = [
            (center[0], y1),
            (x2, center[1]),
            (center[0], y2),
            (x1, center[1])
        ]
        pygame.draw.polygon(surface, color, points)

main()
