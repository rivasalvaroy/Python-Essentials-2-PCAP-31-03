import errno

try:
    stream = open("file", "rb")
    print("existe")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("ausente")
    else:
        print("desconocido")
