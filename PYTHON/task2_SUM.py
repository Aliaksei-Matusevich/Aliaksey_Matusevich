number = int(input()) 
if 0 <= number <= 9 or 0 >= number >= -9 :
    print("Цифра =", number)
if 100 <= number <= 999 or -100 >= number >= -999 :
    hundreds = number // 100
    dozens = (number % 100) // 10
    units = number % 10
    print("Сумма цифр =", hundreds + dozens + units)
if 10 <= number <= 99 or -10 >= number >= -99:
    dozens = number // 10
    units = number % 10
    print("Сумма цифр =", dozens + units)
if 1000 <= number or number <= -1000 :
    print("Wrong answer")