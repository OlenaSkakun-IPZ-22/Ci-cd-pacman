import time

class PacMan:
    def __init__(self, x, y, game_manager):
        self.x = x
        self.y = y
        self.lives = 3
        self.score = 0
        self.game_manager = game_manager
        self.power_mode = False  # Чи активний енергоджайзер
        self.power_mode_end_time = 0

    def move(self, direction, maze):
        """Переміщення Pac-Man у заданому напрямку"""
        new_x, new_y = self.x, self.y
        if direction == "UP":
            new_y -= 1
        elif direction == "DOWN":
            new_y += 1
        elif direction == "LEFT":
            new_x -= 1
        elif direction == "RIGHT":
            new_x += 1

        if not maze.is_wall(new_x, new_y):
            self.x, self.y = new_x, new_y

            # Перевіряємо, чи Pac-Man з'їв точку або енергоджайзер
            if maze.grid[new_y][new_x] == ".":
                self.score += 10
                maze.grid[new_y][new_x] = " "
            elif maze.grid[new_y][new_x] == "O":
                self.activate_power_mode()
                maze.grid[new_y][new_x] = " "

            # Перевірка зіткнення з привидами
            for ghost in self.game_manager.ghosts:
                if self.x == ghost.x and self.y == ghost.y:
                    if self.power_mode:
                        print("🌀 Pac-Man з'їв привида!")
                        self.game_manager.ghosts.remove(ghost)  # Видаляємо привида
                        self.score += 200  # Додаємо очки
                    else:
                        print("❌ Pac-Man з'їдений!")
                        self.lives -= 1  # Втрачаємо життя
                        if self.lives <= 0:
                            self.game_manager.game_over = True

    def activate_power_mode(self):
        """Активація енергоджайзера (Pac-Man може їсти привидів)"""
        print("⚡️ Pac-Man активував енергоджайзер!")
        self.power_mode = True
        self.power_mode_end_time = time.time() + 5  # Діє 5 секунд

    def update(self):
        """Оновлення стану Pac-Man (перевірка закінчення ефекту енергоджайзера)"""
        if self.power_mode and time.time() > self.power_mode_end_time:
            print("🕒 Час енергоджайзера вичерпано!")
            self.power_mode = False  # Вимикаємо режим

    def reset_position(self, start_x=1, start_y=1):
        """Скидає позицію Pac-Man у початкову"""
        self.x = start_x
        self.y = start_y