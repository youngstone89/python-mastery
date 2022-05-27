seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasonsEnum = enumerate(seasons)
print(str(seasonsEnum))
for k,v in seasonsEnum:
    print(k,v)

seasonsList = list(enumerate(seasons))

print(seasonsList)

seasonsList=list(enumerate(seasons, start=1))

print(seasonsList)


for k,v in seasonsList:
    print(k,v)


for s in seasonsList:
    print(s)
    print(type(s))