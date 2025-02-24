import random
import time

class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.previous_tile = ' '  # Що було під привидом перед тим, як він зайшов у клітинку
        self.eatable = False  # Чи їстівний привид
        self.color = (255, 0, 0)  # Червоний за замовчуванням
        self.eatable_timer = 0  # Час, коли привид повернеться до нормального стану

    def update(self, game_manager):
        """Оновлення стану привидів (чи їстівні вони)"""
        pass

    def move(self, maze):
        """Рух привида випадковим напрямком"""
        pass