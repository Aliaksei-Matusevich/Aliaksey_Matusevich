arr = tuple(map(int, input().split()))
l = 5
r = 2
if l >= 0 or r >= 0:
    arr2 = arr[l:r:-1]
    arr3 = tuple(sorted(arr2)[::-1])
    print(arr3)
elif l <= -1 or r <= -1:
    arr2 = arr[r:l:-1]
    arr3 = tuple(sorted(arr2)[::-1])
    print(arr3)
elif l <= -1 or r >= 0:
    arr2 = arr[l:r:-1]
    arr3 = tuple(sorted(arr2)[::-1])
    print(arr3)
elif l >= 0 or r <= -1:
    arr2 = arr[l:r:-1]
    arr3 = tuple(sorted(arr2)[::-1])
    print(arr3)
else:
    print("invalid borders")