n = int(input())
cities = dict()
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