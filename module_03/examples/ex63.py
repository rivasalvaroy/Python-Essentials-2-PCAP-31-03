class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name


class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name


mus = AncientMouse("Caesar")
print(mus)
