class ExampleClass:
    varia = 1

    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print('-'*65)

print(ExampleClass.__dict__)

print('-'*65)

print(example_object.__dict__)
print(example_object.varia)
