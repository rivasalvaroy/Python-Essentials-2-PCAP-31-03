try:
    i = int("¡Hola!")
except Exception as e:
    print(e)
    print(e.__str__())


try:
    print(17/0)
except ZeroDivisionError as z:
    print(z)
    print(z.__str__())


print(17/0)
