tt = (1, 2, (3, 4))
print(hash(tt))

# hash((1, 2, [3, 4]))

print(hash((1, 2, frozenset([3, 4]))))
