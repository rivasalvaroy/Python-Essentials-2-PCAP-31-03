# Este código no puede ser terminado presionando Ctrl-C.
import sys
from time import sleep


seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")
        sleep(2)
        sys.exit()
