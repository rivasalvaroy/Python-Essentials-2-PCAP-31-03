class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1


snake = Snake()
snake.increment()

print(snake.victims)
