class Sample:
    gamma = 0  # Class variable.

    def __init__(self):
        self.alpha = 1  # Variable de instancia.
        self.__delta = 3  # Variable de instancia privada.


obj = Sample()
# Otra variable de instancia (que existe solo dentro de la instancia "obj").
obj.beta = 2
print(obj.__dict__)
