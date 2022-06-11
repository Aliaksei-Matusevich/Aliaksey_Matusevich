arr = list(map(int, input().split()))
l = 5
r = 2
if l >= 0 or r >= 0:
    arr2 = arr[l:r:-1]
    arr2.sort(reverse=True)
    print(arr2)
elif l <= -1 or r <= -1:
    arr2 = arr[r:l:-1]
    arr2.sort(reverse=True)
    print(arr2)
elif l <= -1 or r >= 0:
    arr2 = arr[l:r:-1]
    arr2.sort(reverse=True)
    print(arr2)
elif l >= 0 or r <= -1:
    arr2 = arr[l:r:-1]
    arr2.sort(reverse=True)
    print(arr2)
else:
    print("invalid borders")