from os import strerror

counters = {chr(ch): 0 for ch in range(ord("a"), ord("z") + 1)}
file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()
    file = open(file_name + '.hist', 'wt')
    '''Nota: hemos utilizado una lambda para acceder a los elementos 
    del directorio y se ha establecido reverse a True para obtener un 
    orden válido.'''
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + " -> " + str(c) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
