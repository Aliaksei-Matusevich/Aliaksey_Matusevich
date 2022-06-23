lst = list(map(int, input().split()))
def get_ranges(lst):
    s = e = None
    for i in sorted(lst):
        if s is None:
            s = e = i
        elif i == e or i == e + 1:
            e = i
        else:
            yield (s, e)
            s = e = i
    if s is not None:
        yield (s, e)
sorted_range = ['%d' % s if s == e else '%d-%d' % (s, e) for (s, e) in get_ranges(lst)]
print(repr(','.join(sorted_range)))