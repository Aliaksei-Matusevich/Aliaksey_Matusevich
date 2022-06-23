a = b = 1
n = int(input())
while n > 2:
    a , b = b, a + b
    n -= 1
print(b)  