class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("oculto")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("fallido")

obj._Classy__hidden()
