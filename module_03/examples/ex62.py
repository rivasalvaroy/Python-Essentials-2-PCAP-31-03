class Mouse:
    population = 0

    def __init__(self, name):
        Mouse.population += 1
        self.name = name

    def __str__(self):
        return "Hola, mi nombre es " + self.name


class LabMouse(Mouse):
    pass


professor_mouse = LabMouse("Profesor Mouse")
print(professor_mouse, Mouse.population)
