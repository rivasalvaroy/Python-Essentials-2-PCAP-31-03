class Snake:
    def __init__(self, victims):
        self.victims = victims

    def increment(self):
        self.victims += 1


snake = Snake(7)
snake.increment()

print(snake.victims)
