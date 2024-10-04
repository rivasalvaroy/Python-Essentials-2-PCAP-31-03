class Snake:
    pass


class Python(Snake):
    pass


print(Python.__name__, 'es una', Snake.__name__)
print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__)
