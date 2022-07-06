lst = ['сложнее', 'задачу', 'решить', 'можно', 'Теперь']
def print_forward(lst):
    if len(lst) != None:
        print(lst.pop(-1))
        return lst
print_forward(lst)
print_forward(lst)
print_forward(lst)
print_forward(lst)
print_forward(lst)