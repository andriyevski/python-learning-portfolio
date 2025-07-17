top_country = ['Canada','USA','France','New zeland','Finland']
print(top_country)
print(sorted(top_country))
top_country.reverse()
print(top_country)
top_country.reverse()
print(top_country)
top_country.sort()
print(top_country)
top_country.sort(reverse = True)
print(top_country)

## Guests list task
#
top_guests = ['Mike Tyson','Elon Musk','Bill Gates']
print(len(top_guests))

rank_lang = ['Python','C#','C++','PHP']
rank_lang.append('C')
rank_lang.sort()
rank_lang.reverse()
rank_lang.pop()
rank_lang.insert(0,'Golang')
rank_lang.remove('C++')
del rank_lang[1]
print(sorted(rank_lang))
