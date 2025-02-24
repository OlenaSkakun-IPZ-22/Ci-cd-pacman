import pygame
import sys
from game_state import GameState
from maze import Maze
from game.game_manager import GameManager

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Створення гри
maze = Maze()
game = GameManager(maze)
game_state = GameState()

#намалювати стіни


#намалювати самого пакмена



#намалювати привида



# Функція для відображення рахунку та кількості життів




# Основний цикл гри
running = True
while running:
    screen.fill(BLACK)  # Очищення екрану

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Оновлення
    clock.tick(10)  # Обмеження FPS до 10
pygame.quit()
sys.exit()
