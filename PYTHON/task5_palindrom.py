number = int(input())
reverse_number = 0
copy_of_number = number
while copy_of_number != 0:
    var = copy_of_number % 10
    reverse_number = reverse_number * 10 + var
    copy_of_number = int(copy_of_number / 10)
if number == reverse_number:
    print(f"Число - {number} является палиндромом")
else:
    print(f"Число - {number} не является палиндромом")