import random
import os
import msvcrt

class SnakeGame:
    def __init__(self):
        self.width = os.get_terminal_size().columns
        self.height = os.get_terminal_size().lines - 3
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = "right"
        self.normal_food = self.generate_food("π")
        self.special_food = self.generate_food("X")
        self.obstacles = self.generate_obstacles()
        self.score = 0
        self.special_food_eaten = 0
        self.game_over = False

    def generate_obstacles(self):
        num_obstacles = (self.width * self.height) // 20  # 5% of the game screen
        obstacles = set()
        for _ in range(num_obstacles):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if all((x + i, y) not in self.snake and (x + i, y) not in obstacles for i in range(5)):
                    obstacles.update((x + i, y) for i in range(5))
                    break
        return obstacles

    def generate_food(self, symbol):
        while True:
            empty_cells = [
                (x, y)
                for y in range(self.height)
                for x in range(self.width)
                if (x, y) not in self.snake and (x, y) not in self.generate_obstacles()
            ]
            if empty_cells:
                return (*random.choice(empty_cells), symbol)

    def display(self):
        print("\033c")  # Clear the console
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.snake:
                    print("█", end="")
                elif (x, y) == self.normal_food[:2]:
                    print(self.normal_food[2], end="")
                elif (x, y) == self.special_food[:2]:
                    print(self.special_food[2], end="")
                elif (x, y) in self.obstacles:
                    print("O", end="")
                else:
                    print(" ", end="")
            print()

    def update_direction(self, key):
        if key == b"\xe0":
            key = msvcrt.getch()
            if key == b"H" and self.direction != "down":
                self.direction = "up"
            elif key == b"P" and self.direction != "up":
                self.direction = "down"
            elif key == b"M" and self.direction != "left":
                self.direction = "right"
            elif key == b"K" and self.direction != "right":
                self.direction = "left"

    def move(self):
        head = self.snake[0]
        if self.direction == "up":
            new_head = (head[0], head[1] - 1)
            if new_head[1] < 0:
                new_head = (new_head[0], self.height - 1)
        elif self.direction == "down":
            new_head = (head[0], head[1] + 1)
            if new_head[1] >= self.height:
                new_head = (new_head[0], 0)
        elif self.direction == "left":
            new_head = (head[0] - 1, head[1])
            if new_head[0] < 0:
                new_head = (self.width - 1, new_head[1])
        elif self.direction == "right":
            new_head = (head[0] + 1, head[1])
            if new_head[0] >= self.width:
                new_head = (0, new_head[1])
        self.snake.insert(0, new_head)
        if new_head == self.normal_food[:2]:
            self.score += 1
            self.normal_food = self.generate_food("π")
        elif new_head == self.special_food[:2]:
            if len(self.snake) > 1:
                self.snake.pop()
                self.special_food_eaten += 1
            self.special_food = self.generate_food("X")
        else:
            self.snake.pop()
        self.check_collision()

    def run(self):
        print(f"Score: {self.score}, Special Food Eaten: {self.special_food_eaten}")
        while not self.game_over:
            self.display()
            self.update_direction(msvcrt.getch())
            self.move()
            self.check_collision()
            self.check_food()
            self.check_game_over()
            self.update_game()

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:] or head in self.obstacles:
            self.game_over = True

    def check_food(self):
        if self.score >= 3 and self.special_food_eaten < 3:
            self.special_food = self.generate_food("X")

    def check_game_over(self):
        if len(self.snake) == self.width * self.height:
            self.game_over = True
        if len(self.snake) == self.width * self.height:
            self.game_over = True
            print(f"Game Over! Score: {self.score}, Special Food Eaten: {self.special_food_eaten}")

    def update_game(self):
        pass

game = SnakeGame()
game.run()