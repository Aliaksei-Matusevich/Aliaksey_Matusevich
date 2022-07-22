import json
with open('top 250 films/ratings.list.txt', 'r', encoding="cp1252") as f, open('250top.txt', 'w') as outfile: 
        data = f.readlines()
        s =  outfile.writelines(data[28:278])


with open('250top.txt', 'r') as finp, open('name250top.txt', 'w') as name:
        data = [line.strip() for line in finp.readlines()]
        columns = [i.split() for i in data]
        name_of_films = [(i[3:-1]) for i in columns]
        json.dump(name_of_films, name, indent='')

with open('250top.txt', 'r') as finp, open('ratings films.txt', 'w') as ratings:
        data = [line.strip() for line in finp.readlines()]
        columns = [i.split() for i in data]
        rating = [(i[2]) for i in columns]
        gistogramm_of_ratings = {w: rating.count(w) for w in set(rating)}
        json.dump(gistogramm_of_ratings, ratings, indent=' ')

with open('250top.txt', 'r') as finp, open('year.txt', 'w') as years:
        data = [line.strip() for line in finp.readlines()]
        columns = [i.split() for i in data]
        year = [(i[-1]).replace("(", " ").replace(")", ' ') for i in columns]
        gistogramm_of_years = {w: year.count(w) for w in set(year)}
        json.dump(gistogramm_of_years, years, indent=' ')