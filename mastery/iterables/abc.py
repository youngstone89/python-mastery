s = 'ABC'

# for loop
for char in s:
    print(char)


it = iter(s)  # create iterator from interable

# using iterator
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
