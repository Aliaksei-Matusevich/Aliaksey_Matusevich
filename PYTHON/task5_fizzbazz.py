lst = [ i for i in range(1,100)]
for index, number in enumerate(lst):
    if number % 3 == 0:
      lst[index] = "fizz"
    if number % 5 == 0:
      lst[index] = "bazz"
    if number % 3 == 0 and number % 5 == 0:
      lst[index] = "fizzbazz"
print(lst)