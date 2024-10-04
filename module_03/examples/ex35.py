class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star('Sol', 'Via Lactea')
print(sun)
print(sun.__str__())
