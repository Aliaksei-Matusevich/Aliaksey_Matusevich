'''1. Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv'].
   2. Используйте на предыдущий список slice чтобы получить следующий: ['xy', 'xv', 'yz'].
   3. Используйте генератор списков чтобы получить следующий ['1x', '2x', '3x', '4x'].
   4. Одной строкой (и одним выражением) удалите элемент '2x' из прошлого списка и напечатайте его.
   5. Скопируйте список и добавьте в него элемент 2x так чтобы в исходном списке этого элемента не было.
Задания разделены принтом=)'''
lst = ["x", "y"]                                                                                        
lst_rev = ["y", "z", "v"]                             
g = [(x,y) for x in lst for y in lst_rev]      
print(g)
g = [(x,y) for x in lst for y in lst_rev][::2]
print(g)
print()
digits_list = [element + ('x') for element in ('1', '2', '3', '4')]
print(digits_list)
print()
digits_list = [element + ('x') for element in ('1', '2', '3', '4')][1:2]
print(digits_list)
print()
digits_list = [element + ('x') for element in ('1', '3', '4')]
digits_list.append('2x')
print(digits_list)