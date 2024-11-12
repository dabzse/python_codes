import pygame
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('"Flower"')
clock = pygame.time.Clock()

colors = [(255, 0, 0), (100, 149, 237), (0, 255, 0), (0, 255, 127), (173, 216, 230), (0, 0, 255)]
background_color = (0, 0, 0)

radius = 160
total_circles = 36
segments = 360

def draw_circle_segment(x_center, y_center, radius, color, start_angle, end_angle):
    paused = False
    for angle in range(start_angle, end_angle):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_RETURN:
                    return False
                if event.key == pygame.K_q:
                    pygame.quit()
                    return True

        if not paused:
            x = x_center + radius * math.cos(math.radians(angle))
            y = y_center + radius * math.sin(math.radians(angle))
            screen.set_at((int(x), int(y)), color)
            pygame.display.flip()
            pygame.time.delay(1)
    return False

def draw_circles():
    angle_offset = 0
    for i in range(total_circles):
        color = colors[i % len(colors)]

        x_center = width // 2 + radius * math.cos(math.radians(270 + angle_offset))
        y_center = height // 2 + radius * math.sin(math.radians(270 + angle_offset))

        for segment in range(0, segments, 10):
            if draw_circle_segment(x_center, y_center, radius, color, segment, segment + 10):
                return

        angle_offset += 10

def rotate_circles():
    angle_offset = 0
    rotating = True
    paused = False
    while rotating:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_RETURN:
                    rotating = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    return

        if not paused:
            screen.fill(background_color)
            for i in range(total_circles):
                color = colors[i % len(colors)]

                x_center = width // 2 + radius * math.cos(math.radians(270 + angle_offset))
                y_center = height // 2 + radius * math.sin(math.radians(270 + angle_offset))

                pygame.draw.circle(screen, color, (int(x_center), int(y_center)), radius, 1)

                angle_offset += 10

            pygame.display.flip()
            angle_offset += 1
            clock.tick(60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(background_color)
                draw_circles()
                rotate_circles()
            if event.key == pygame.K_RETURN:
                screen.fill(background_color)
                draw_circles()
                rotate_circles()
            if event.key == pygame.K_q:
                running = False

    clock.tick(60)

pygame.quit()

