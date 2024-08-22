from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City(name='tokyo', country='JP', population=36.993,
             coordinates=(123.111, 234.111))

print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.123, LatLong(123.123, 123.123))
delhi = City._make(delhi_data)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key+":", value)
