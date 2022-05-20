from collections import Counter



c = Counter('gallahad')
c = Counter({'red':4,'blue':2})
c = Counter(cats=4, dogs=8)
print(c.elements())
print(c.most_common(3))


c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
