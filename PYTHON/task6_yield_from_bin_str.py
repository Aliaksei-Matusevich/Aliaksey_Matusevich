import random
def binary_string_gen(start, end, num):
    lst = []
    for i in range(num):
        lst.append(random.randint(start, end))
    yield from lst
string = list(binary_string_gen(0, 1, 3))
print(string[0], string[1], string[2])