any_list = [1, 2, 3, 4]

even_list = list(map(lambda x: x+1 if x % 2 == 0 else x, any_list))

even_list_two = list(map(lambda x: x | 1, any_list))

print(even_list)

print(even_list_two)
