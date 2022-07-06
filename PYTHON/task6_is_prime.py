num = int(input('Введите число: '))
simplex = []
def is_prime():
    res = [i for i in range(1, num + 1) if num % i == 0]
    if num == 0 or num == 1 or res[1] != num:
        print(f'Число {num} не является простым')
        return any(simplex)
    elif res[0] == 1 and res[1] == num:
        print(f'Число {num} простое')
        simplex.append(num)
        return all(simplex)
print(is_prime())  
 