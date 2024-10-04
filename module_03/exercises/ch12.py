class Dog:
    kennel = 0

    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1

    def __str__(self):
        return self.breed + " dice: ¡Guau!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, corderito!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, intruso!"


class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + "¡No me gustan las montañas!"


rocky = LowlandDog("Collie")

print(rocky)
