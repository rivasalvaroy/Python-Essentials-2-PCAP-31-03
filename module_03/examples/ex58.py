class Mouse:
    pass


class LabMouse(Mouse):
    pass


print(issubclass(Mouse, LabMouse), issubclass(
    LabMouse, Mouse))  # Imprime "False True"
