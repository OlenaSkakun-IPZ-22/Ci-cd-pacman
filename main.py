import pygame

# Инициализация Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Основний цикл гри
running = True
while running:
    screen.fill((0, 0, 0))  # Очищення екрану

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Оновлення екрану
    clock.tick(10)  # Обмеження FPS

pygame.quit()
