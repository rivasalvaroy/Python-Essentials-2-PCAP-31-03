class Sample:
    def __init__(self):
        self.name = Sample.__name__

    def myself(self):
        print("Mi nombre es " + self.name + " y vivo en " + Sample.__module__)


obj = Sample()
obj.myself()
