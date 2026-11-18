import random 

from config import (
    GRID_WIDTH,
    GRID_HEIGHT,
    INITIAL_SNAKE_LENGTH,
    INITIAL_SPEED,
    MAX_SPEED,
    POINTS_PER_FOOD,
    BONUS_FOOD_POINTS, 
)


class SnakeGame:

    def __init__(self, mode="classic"):

        self.mode = mode

        self.snake = [
            (GRID_WIDTH // 2, GRID_HEIGHT // 2)
            for i in range(INITIAL_SNAKE_LENGTH)
        ]

        self.direction = (1,0)
        self.next_direction = (1,0)


        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED

        self.food = None
        self.bonus_food = None 

        self.obstacles = set()

        self.game_over = False
        self.paused = False 

        self.food_eaten = 0 
        self.spawn_food()

        if self.mode == "Obstacles":
            self.generate_obstacles()

def spawn_food(self):

    empty_cells = [
        (x,y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x,y) not in self.snake
        and (x,y) not in self.obstacles
    ]

    if empty_cells: [
        (x,y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x,y) not in self.snake 
        and (x,y) not in self.obstacles
        and (x,y) != self.food
    ]

    if empty_cells:
        self.bonus_food = 
random.choice(empty_cells)
