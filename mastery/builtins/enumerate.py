seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasonsEnum = enumerate(seasons)

seasonsList = list(enumerate(seasons))

print(seasonsList)

seasonsList=list(enumerate(seasons, start=1))

print(seasonsList)


for k,v in seasonsList:
    print(k,v)