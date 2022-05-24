text = 'Python'

# convert string to list
text_list = list(text)
print(text_list)

# check type of text_list
print(type(text_list))

# Output: ['P', 'y', 't', 'h', 'o', 'n']
#         <class 'list'> 


# empty list
print(list())

# vowel string
vowel_string = 'aeiou'
print(list(vowel_string))

# vowel tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))

# vowel list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))


# vowel set
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set))

# vowel dictionary
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}
print(list(vowel_dictionary))


# objects of this class are iterators
class PowTwo:
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
        
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result

pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))