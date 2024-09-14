from collections import abc
import re
import reprlib

RE_WORD = re.compile('\\w+')


class Setence:

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    # iter() built-in function checks whether __iter__() method has been implemented.
    # otherwise, construct iterator using __getitem__()
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Setence(%s)' % reprlib.repr(self.text)


s = Setence('"The time has come, " the Walrus said."')

print(s)

for w in s:
    print(w)


print(list(s))


iter(s)


class Foo:
    def __iter__(self):
        pass


print(issubclass(Foo, abc.Iterable))

f = Foo()
print(isinstance(f, abc.Iterable))


print(issubclass(Setence, abc.Iterable))
