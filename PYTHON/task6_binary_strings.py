def binary_strings(need, balance=3, string=''):     
    if balance < 0:
        return
    if need == 0:
        if balance == 0:
            print(string)
        return
    binary_strings(need - 1, balance - 1, string + '1')
    binary_strings(need - 1, balance + 1, string + '0')
    binary_strings(need - 1, balance - 1, string + '0')
    binary_strings(need - 1, balance + 1, string + '1')
binary_strings(3)