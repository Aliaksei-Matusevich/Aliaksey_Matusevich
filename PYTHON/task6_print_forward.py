lst = ['Это', 'игрушечный', 'пример', 'не', 'используйте', 'рекурсию', 'для', 'такого']
def print_forward(lst):
    if len(lst) != None:
        print(lst.pop(0))
        return lst
print_forward(lst)
print_forward(lst)
print_forward(lst)
print_forward(lst)
print_forward(lst)
print_forward(lst)
print_forward(lst)
print_forward(lst)
