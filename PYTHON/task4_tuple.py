lst = ['a', 'b', 'c']   
lst_to_tpl = tuple(lst)    #Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
tpl_to_lst = list(lst_to_tpl)    #Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.
a, b, c = "a", 2, "python"    #Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
print(lst_to_tpl, tpl_to_lst, a, b, c)
