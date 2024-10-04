class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return f'{self.name} en {self.galaxy}'


sun = Star('Sol', 'Via Lactea')
print(sun)
print(sun.__str__())
