import math


class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)


try:
    raise NewValueError("Advertencia enemiga",
                        "Alerta roja", "Alta disponibilidad")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')
