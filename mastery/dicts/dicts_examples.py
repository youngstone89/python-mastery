

a = dict(one=1, two=2)
b = {'one': 1, 'two': 2}
c = dict(zip(['one', 'two'], [1, 2]))
d = dict([('one', 1), ('two', 2)])
e = dict({'one': 1, 'two': 2})
print(a == b == c == d == e)
