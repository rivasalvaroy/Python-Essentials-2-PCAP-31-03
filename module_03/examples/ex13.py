class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
print(example_object_1.__dict__, example_object_1.counter)

example_object_2 = ExampleClass(2)
print(example_object_2.__dict__, example_object_2.counter)

example_object_3 = ExampleClass(4)
print(example_object_3.__dict__, example_object_3.counter)
