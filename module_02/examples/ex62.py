from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

# Debemos estar seguros de que angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
