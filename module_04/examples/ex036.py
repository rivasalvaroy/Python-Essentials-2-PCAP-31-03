from os import strerror

try:
    # Un nuevo archivo (newtext.txt) es creado.
    file = open('./files/newtext.txt', 'wt')
    for i in range(10):
        s = "línea #" + str(i+1) + "\n"
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
