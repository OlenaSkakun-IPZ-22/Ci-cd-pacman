class Maze:
    def __init__(self):
        self.grid = [
            list("###############"),
            list("#P..O.....#...#"),
            list("#.#######.#.#.#"),
            list("#.#     #.#  .#"),
            list("#.# ### #.#  .#"),
            list("#.#   # #.GG..#"),
            list("#.### # #####.#"),
            list("#.....#.......#"),
            list("#####.#.#####.#"),
            list("#.....#.#    .#"),
            list("#.#####.# ## .#"),
            list("#.....#.# ## .#"),
            list("#.#####.####..#"),
            list("#O............#"),
            list("###############")
        ]

    def is_wall(self, x, y):
        """Перевіряє, чи є стіна на координатах (x, y)"""
        pass

    def is_point(self, x, y):
        """Перевіряє, чи є точка у комірці"""
        pass

    def is_power_pellet(self, x, y):
        """Перевіряє, чи є енергоджайзер у комірці"""
        pass

    def eat_point(self, x, y):
        """З'їдає точку або енергоджайзер"""
        pass

    def update_position(self, old_x, old_y, new_x, new_y, entity):
        """Оновлює розташування сутності (Pac-Man або привида) у лабіринті"""
        pass