tpl_of_one = 1,  
for two in tpl_of_one:    #Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы  
    two += 1              #последовательно выводились значения 1, 2, 3.
    for three in tpl_of_one:
        three += 2        
    print(tpl_of_one + (two,) + (three,))           
print("Колличество элементов в последовательности:", len(tpl_of_one),",", type(tpl_of_one))