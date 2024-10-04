from os import strerror

try:
    character_counter = line_counter = 0
    for line in open('./files/text.txt', 'rt'):
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
    print("\n\nCaracteres en el archivo: ", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
