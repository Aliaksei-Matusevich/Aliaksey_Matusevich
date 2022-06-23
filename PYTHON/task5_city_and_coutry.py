cities = dict()
n = int(input())
for i in range(n):
    country = input().split()
    for city in country[1:]:
        cities[city] = country[0]
m = int(input())
result = []
for i in range(m):
    city = input()
    result.append(cities[city])    
print(*result, sep='\n')


"""
4
Belarus Minsk Grodno Vitebsk Gomel Brest
Russia Moscow Saint-Petersburg Smolensk
USA New_York Detroit Los_Angeles
Poland Krakow Warsaw Gdansk Belostok
3
Saint-Petersburg
New_York
Los_Angeles
"""