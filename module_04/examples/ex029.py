# Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
stream = open("./files/tzop.txt", "rt", encoding="utf-8")

# Se imprime el contenido del archivo:
print(stream.read())
