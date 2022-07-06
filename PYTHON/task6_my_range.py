def my_range(start, stop, step = 1):
    start -= step
    while True:
        if start > stop and step < 0:
            if (start + step <= stop):
                break
        else:
            if (start + step >= stop):
                break
        start += step
        yield round(start,2)

for i in my_range(9, -1, -1):
    print(i, end=" ")
print()
for i in range(0, 10, 1):
    print(i, end=" ")