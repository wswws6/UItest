import random
import os

class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = [(width//2, height//2)]
        self.direction = (0, 1)  # 初始方向向右（列增加）
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            if (x, y) not in self.snake:
                return (x, y)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # 检查边界
        if new_head[0] < 0 or new_head[0] >= self.width or \
           new_head[1] < 0 or new_head[1] >= self.height:
            return False

        # 如果新头位置在蛇身内，则游戏结束
        if new_head in self.snake[1:]:
            return False

        # 吃到食物，蛇身加长，生成新的食物
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:  # 没吃到食物，移除蛇尾
            self.snake.pop()

        # 将新头添加到蛇身前端
        self.snake.insert(0, new_head)

        return True

    def change_direction(self, key):
        directions = {
            'w': (-1, 0),
            'a': (0, -1),
            's': (1, 0),
            'd': (0, 1)
        }
        opposite = {'w': 's', 'a': 'd', 's': 'w', 'd': 'a'}

        new_dir = directions.get(key)
        if new_dir and opposite[key] != str(self.direction):
            self.direction = new_dir

    def draw_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Score:", self.score)
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = '#'
                if (x, y) == self.food:
                    cell = '*'
                elif (x, y) in self.snake:
                    cell = 'O'
                row.append(cell)
            print(''.join(row))

    def play(self):
        while True:
            self.draw_game()
            key = input().lower()
            self.change_direction(key)
            if not self.move_snake():
                print("Game Over! Your score was:", self.score)
                break


if __name__ == "__main__":
    game = SnakeGame()
    game.play()
