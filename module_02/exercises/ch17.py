def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
            continue
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: el valor no esta dentro del rango permitido (" +
                  str(min) + ".." + str(max) + ")")
    return value


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
