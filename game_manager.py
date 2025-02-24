class GameManager:
    def __init__(self, maze):
        self.pacman = PacMan(1, 1, self)
        self.ghosts = [Ghost(6, 5), Ghost(8, 5), Ghost(10, 5)]
        self.maze = maze
        self.game_state = GameState()
        self.game_over = False

    def update_game(self):
        """Оновлення гри після кожного кроку"""
        pass

    def check_win_condition(self):
        """Перевіряє, чи всі точки зібрані"""
        pass